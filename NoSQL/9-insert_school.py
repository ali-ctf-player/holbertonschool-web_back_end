#!/usr/bin/env python3
"""It is doc string"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """It is doc string"""

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
