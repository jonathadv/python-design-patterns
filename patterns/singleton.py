"""
********************
Singleton Pattern
********************

Description from Wikipedia:

*"the singleton pattern is a software design pattern that
restricts the instantiation of a class to one 'single' instance.
This is useful when exactly one object is needed to coordinate
actions across the system."*

.. warning:: *"Critics consider the singleton to be an anti-pattern
    in that it is frequently used in scenarios where it is not beneficial,
    introduces unnecessary restrictions in situations where a sole instance
    of a class is not actually required, and introduces global state into an application."*

Source: https://en.wikipedia.org/wiki/Singleton_pattern

The more pythonic way to implement a singleton is by creating
a decorator to store the decorated class instances.
"""


def singleton(cls):
    """
    This decorator ensures that only one instance of
    the decorated class will be created in runtime.

    :param cls: a class to be decorated as singleton
    :type cls: class

    Example:
        A decorated class that displays its own `id(self)`
        will always return the same value.

    >>> @singleton
    >>> class SingletonExample:
    >>>    def __init__(self):
    >>>        self.own_id: int = id(self)
    >>>    def __repr__(self):
    >>>        return f"{self.__class__.__name__}(id={self.own_id})"
    >>>
    >>> SingletonExample()
    SingletonExample(id=140472046362688)
    >>> SingletonExample()
    SingletonExample(id=140472046362688)
    >>> SingletonExample() is SingletonExample()
    True

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
        self.own_id: int = id(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.own_id})"
