import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global submatriz
        undertest = __import__(module)
        submatriz = getattr(undertest, 'submatriz', None)

    def test_exemplos(self):
        M = [
            [11, 12, 13, 14, 15, 16],
            [21, 22, 23, 24, 25, 26],
            [31, 32, 33, 34, 35, 36],
            [41, 42, 43, 44, 45, 46],
            [51, 52, 53, 54, 55, 56],
            [61, 62, 63, 64, 65, 66],
        ]
        assert submatriz(M, 1, 3, 3, 4) == [
            [24, 25],
            [34, 35],
            [44, 45],
        ]
    
        assert submatriz(M, 2, 3, 5, 7) == None
    

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
