#!/usr/bin/env python3
"""A python function that inserts a new document into a collection
based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a document into a collection"""
    return mongo_collection.insert(kwargs)
