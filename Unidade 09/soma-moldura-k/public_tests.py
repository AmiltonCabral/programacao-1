import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
soma_moldura = getattr(undertest, 'soma_moldura', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        M = [[1,  2,  3,  4 ], [5,  6,  7,  8 ], [9,  10, 11, 12], [14, 15, 16, 17]]
        assert soma_moldura(M, 0) == 106

    def test_exemplo2(self):
        M = [[1,  2,  3,  4 ], [5,  6,  7,  8 ], [9,  10, 11, 12], [14, 15, 16, 17]]
        assert soma_moldura(M, 0) == 106
        assert soma_moldura(M, 1) == 34
     
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
