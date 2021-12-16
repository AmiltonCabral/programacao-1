import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
rotaciona_ds = getattr(undertest, 'rotaciona_ds', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [14, 15, 16, 17]]
        assert rotaciona_ds(m, 'cima') == None
        assert m == [[1,  2,  3,  7 ], [5,  6, 10,  8 ], [9, 14, 11,  12], [4, 15, 16,  17]]

    def test_exemplo2(self):
        m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [14, 15, 16, 17]]
        assert rotaciona_ds(m, 'baixo') == None
        assert m == [[1,  2,  3,  14], [5,  6,  4,  8 ], [9,  7,  11, 12], [10, 15, 16, 17]]
     
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
