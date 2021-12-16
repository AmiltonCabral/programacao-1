import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global noves_fora
        undertest = __import__(module)
        noves_fora = getattr(undertest, 'noves_fora', None)

    def test_exemplo(self):
        assert noves_fora([4]) == (4, [[4]])
        assert noves_fora([9]) == (0, [[9], [0]])
        assert noves_fora([9, 9]) == (0, [[9, 9], [0]])
        assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1], [7, 5, 4, 3, 1], [4, 3, 3, 1], [7, 3, 1], [1, 1], [2]])

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
