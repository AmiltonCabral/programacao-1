import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global rotaciona90
        undertest = __import__(module)
        rotaciona90 = getattr(undertest, 'rotaciona90', None)


    def test_simples(self):
        I = [[1, 2, 3, 4, 5],
             [2, 3, 4, 5, 6],
             [3, 4, 5, 6, 7],
             [4, 5, 6, 7, 8]]

        R = rotaciona90(I)
        assert R == [[4, 3, 2, 1],
                     [5, 4, 3, 2],
                     [6, 5, 4, 3],
                     [7, 6, 5, 4],
                     [8, 7, 6, 5]]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
