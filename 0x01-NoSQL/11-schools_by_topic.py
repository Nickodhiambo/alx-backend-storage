#!/usr/bin/env python3
"""A function that queries a mongoDB collection for a list
of schools with a topic passed as argument
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools with a given topic"""
    if mongo_collection is not None:
        return mongo_collection.find({"topics": topic})
