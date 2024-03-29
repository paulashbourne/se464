from mongoengine import Document, EmbeddedDocument
from bson import ObjectId

# A wrapper around mongoengine's Document class to provide additional
# functionality for easier queries
class BaseDocument(Document):
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    # Proxies to constructor
    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    # Finds entities in the database
    # query  - json query
    # limit  - integer
    # offset - integer
    # sort   - list of tuples, where each tuple has a field name
    #          and a direction (+1 or -1)
    #          Example: sort=[('name', 1)] sorts by name ascending
    #                   sort=[('name', -1)] sorts by name descending
    @classmethod
    def find(cls, query, limit=None, offset=None, sort=None):
        queryset = cls.objects.filter(__raw__ = query)
        if offset is not None:
            queryset = queryset.skip(offset)
        if limit is not None:
            queryset = queryset.limit(limit)
        if sort is not None:
            sorts = []
            for fieldName, direction in sort:
                directionPrefix = '+' if direction >= 0 else '-'
                sorts.append(directionPrefix + fieldName)
            queryset = queryset.order_by(*sorts)
        return list(queryset)

    # Similar to find_one, but search is limited to a single result
    @classmethod
    def find_one(cls, query):
        result = cls.find(query, limit=1)
        if len(result):
            return result[0]
        else:
            return None

    # Attempts to cast a variable to different types before querying
    @classmethod
    def cast_value(cls, value):
        try:
            value = ObjectId(value)
        except: pass
        return value

    # Find a single document by id
    @classmethod
    def by_id(cls, id):
        return cls.find_one({'_id' : ObjectId(id)})

    # Find a list of documents by a of ids
    @classmethod
    def by_ids(cls, ids):
        ids = map(lambda id: ObjectId(id), ids)
        return cls.find({'_id' : {'$in' : ids}})

    # Same as above, but return a dict {document.id : document}
    @classmethod
    def by_ids_dict(cls, ids):
        return dict([(c.id, c) for c in cls.by_ids(ids)])

    def set(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        self.save()

    # Specify fields to be included in the default to_dict function
    @classmethod
    def dict_include(cls):
        return []

    # Converts a document to a dict
    #
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
            if type(value) is list:
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
                if type(value) is ObjectId:
                    return str(value)
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
    def validate_fields(cls, fields):
        return True, ""

    def __repr__(self):
        return "<%s(id='%s')>" % (
            self.__class__.__name__,
            self.id
        )
