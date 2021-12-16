import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global gera_triangular_inferior
        undertest = __import__(module)
        gera_triangular_inferior = getattr(undertest, 'gera_triangular_inferior', None)


    def test_simples(self):
        I = [[1, 2, 3, 4],
             [5, 6, 2, 4],
             [2, 7, 8, 1],
             [4, 5, 6, 7]]

        gera_triangular_inferior(I)
        assert I == [[1, 0, 0, 0],
                     [7, 6, 0, 0],
                     [5, 9, 8, 0],
                     [8, 9, 7, 7]]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
