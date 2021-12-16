import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global soma_matriz_interna
        undertest = __import__(module)
        soma_matriz_interna = getattr(undertest, 'soma_matriz_interna', None)

    def test_1(self):
        M2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
        assert soma_matriz_interna(M2, (1,1),(2,2)) == 5 + 6 + 8 + 9
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
