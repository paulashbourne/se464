from mongoengine import Document

class BaseDocument(Document):
    meta = {'allow_inheritance': True}

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def dict_include(cls):
        return []

    # _seen is used to store list of objects which this
    # method is called on in the recursion tree.
    # This is to prevent circular recursion over relationships.
    def to_dict(self, cast=True, _seen = None):
        if _seen is None:
            _seen = [self]
        else:
            _seen.append(self)

        def transform_value(value):
            from datetime import datetime, date
            from decimal import Decimal
            if type(value) is list or type(value):
                return map(transform_value, value)
            elif issubclass(value.__class__, BaseDocument):
                if value in _seen:
                    return None
                else:
                    return value.to_dict(
                        cast   = cast,
                        _seen  = _seen
                    )
            if cast:
                if type(value) is datetime or type(value) is date:
                    return value.strftime("%s")
            return value

        result = {}
        for key in self.dict_include():
            value = self.get_value(key)
            result[key] = transform_value(value)
        return result

    @staticmethod
    def get_key(inst, key):
        keys = key.split('.', 1)
        result = getattr(inst, keys[0])
        if len(keys) > 1:
            return result.get_key(".".join(keys[1:]))
        else:
            return result

    def get_value(self, key):
        return BaseDocument.get_key(self, key)

    @classmethod
    def by_id(cls, id):
        return cls.db_session.query(cls).filter_by(id = id).first()

    @classmethod
    def by_ids(cls, ids):
        return cls.db_session.query(cls).filter(cls.id.in_(ids)).all()

    @classmethod
    def by_ids_dict(cls, ids):
        return dict([(c.id, c) for c in cls.by_ids(ids)])

    @classmethod
    def create(cls, commit = True, **kwargs):
        item = cls(**kwargs)
        cls.db_session.add(item)
        if commit:
            cls.db_session.commit()
            cls.db_session.refresh(item)
        return item

    @classmethod
    def default_order(cls):
        return cls.id.asc()

    @classmethod
    def apply_query_options(cls, query, **kwargs):
        if 'search' in kwargs and kwargs['search']:
            if not kwargs['search_field']:
                raise RuntimeError("Search field not specified")
            column = cls.get_column(kwargs['search_field'])
            query = query.filter(column.like("%%%s%%" % kwargs['search']))
        if 'order_by' in kwargs:
            query = query.order_by(cls.get_sort(*kwargs['order_by']))
        else:
            query = query.order_by(cls.default_order())
        if 'start' in kwargs:
            query = query.offset(kwargs['start'])
        if 'count' in kwargs:
            query = query.limit(kwargs['count'])
        return query

    @classmethod
    def validate_fields(cls, fields):
        return True, ""

    @classmethod
    def validate(cls, fields):
        return cls.validate_fields(fields)

    def validate_update(self, updates):
        return self.validate_fields(updates)

    @classmethod
    def column_aliases(cls):
        return {}

    @classmethod
    def get_column(cls, name):
        aliases = cls.column_aliases()
        if name in aliases:
            name = aliases[name]
        return BaseTable.get_key(cls, name)

    @classmethod
    def get_sort(cls, sort, direction):
        column = cls.get_column(sort)
        if direction == 'asc':
            return column.asc()
        else:
            return column.desc()

    @classmethod
    def query(cls):
        return cls.db_session.query(cls)

    def __repr__(self):
        return "<%s(id='%d')>" % (
            self.__class__.__name__,
            self.id
        )
