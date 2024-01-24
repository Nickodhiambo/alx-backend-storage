#!/usr/bin/env python3
"""Redis basics"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class are called"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """A Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """This method store the history of inputs and outputs for a
    particular function
    """

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """A Wrapper function"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output

    return wrapper


class Cache():
    """A class that stores data"""
    def __init__(self):
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[bytes, int, str, float]) -> str:
        """Store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float, None]:
        """Retrieve data"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve data as string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Retrieve data as integer"""
        return self.get(key, int)
