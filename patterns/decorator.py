"""
Decorator Pattern
https://en.wikipedia.org/wiki/Decorator_pattern

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