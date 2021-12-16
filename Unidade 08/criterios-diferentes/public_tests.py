#!/usr/bin/env python
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
ordena = getattr(undertest, 'ordena', None)

class PublicTests(unittest.TestCase):

    def test_1_base(self):
        l1 = [8, 12, 78, 79, 511]
        l2 = [302, 121, 8, 7]
        assert ordena(l1, l2) == [7, 8, 8, 12, 78, 79, 121, 302, 511]
        assert l1 == [8, 12, 78, 79, 511]
        assert l2 == [302, 121, 8, 7]
        
    def test_exemplo(self):
        assert ordena([3.9,4.0],[1.9]) == [1.9,3.9,4.0]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
