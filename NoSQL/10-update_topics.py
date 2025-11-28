#!/usr/bin/env python3
"""It is doc string"""


def update_topics(mongo_collection, name, topics):
    """It is doc string"""

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics"}:topics}
    )
