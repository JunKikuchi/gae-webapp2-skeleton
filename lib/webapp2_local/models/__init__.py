from google.appengine.ext import ndb

class Unique(ndb.Expando):
    @classmethod
    def create(cls, _id, **properties):
        key = ndb.Key(cls, _id)
        def txn():
            if not key.get():
                return cls(key=key, **properties).put()
            else:
                return None
        return ndb.transaction(txn)

    @classmethod
    def create_multi(cls, ids):
        created  = []
        existing = []

        for _id in ids:
            key = ndb.Key(cls, _id)
            def txn():
                if not key.get():
                    created.append(cls(key=key).put())
                else:
                    existing.append(key)
            ndb.transaction(txn)

        if existing == []:
            return True, created
        else:
            ndb.delete_multi(created)
            return False, existing
