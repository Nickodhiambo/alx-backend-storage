#!/usr/bin/env python3
""" A python function that lists all documents in a mongoDB"""

import pymongo


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    if mongo_collection is None:
        return []
    all_docs = mongo_collection.find()
    return [doc for doc in all_docs]
