"""
Singleton Pattern
https://en.wikipedia.org/wiki/Singleton_pattern

A more pythonic way to do it is by creating
a decorator to store the decorated class instance.
"""


def singleton(cls):
    """
    Create a single instance of a class.

    :param cls: a class to be decorated
    :type cls: class
    """
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class SingletonExample:
    """
    SingletonExample

    A class that stores a value of its id.
    """
    def __init__(self):
        self.value: int = id(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"