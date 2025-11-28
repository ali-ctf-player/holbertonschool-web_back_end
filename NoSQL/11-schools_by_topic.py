#!/usr/bin/env python3
"""It is doc string"""


def schools_by_topic(mongo_collection, topic):
    """It is doc string"""

    return list(mongo_collection.find({"topics": topic}))
