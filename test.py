from unittest import TestCase
from patterns.singleton import SingletonExample

class SingletonTestCase(TestCase):
    def test_new_instance(self):
        """Test multiple calls to a singleton class"""
        self.assertIs(SingletonExample(), SingletonExample())
        self.assertEqual(SingletonExample().value, SingletonExample().value)
        self.assertEqual(hash(SingletonExample()), hash(SingletonExample()))
