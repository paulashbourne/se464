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
        return cls.find_one({'_id' : id})

    @classmethod
    def by_ids(cls, ids):
        return cls.find({'_id' : {'$in' : ids}})

    @classmethod
    def by_ids_dict(cls, ids):
        return dict([(c.id, c) for c in cls.by_ids(ids)])

    @classmethod
    def validate_fields(cls, fields):
        return True, ""

    @classmethod
    def validate(cls, fields):
        return cls.validate_fields(fields)

    def validate_update(self, updates):
        return self.validate_fields(updates)

    def __repr__(self):
        return "<%s(id='%s')>" % (
            self.__class__.__name__,
            self.id
        )
