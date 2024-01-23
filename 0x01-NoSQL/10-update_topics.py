#!/usr/bin/env python3
"""A python function that updates a document based on a name property"""


def update_topics(mongo_collection, name, topics):
    """Updates a document with topics property"""
    if mongo_collection is not None:
        mongo_collection.update_many(
                {"name": name},
                {"$set": {"topics": topics}}
                )
