#!/usr/bin/env python3
"""A python function that inserts a new document into a collection
based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a document into a collection"""
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
