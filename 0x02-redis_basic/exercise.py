#!/usr/bin/env python3
"""Redis basics"""

import redis
import uuid
from typing import Union


class Cache():
    """A class that stores data"""
    def __init__(self):
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, int, str, float]) -> str:
        """Store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
