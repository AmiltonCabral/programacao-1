import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global zera_acima_ou_abaixo
        undertest = __import__(module)
        zera_acima_ou_abaixo = getattr(undertest, 'zera_acima_ou_abaixo', None)

    def test_exemplo_1(self):
        M = [[1,2,3],
             [4,5,6],
             [7,8,9]]
        zera_acima_ou_abaixo(M)
        assert M == [[1,2,3],
                     [0,5,6],
                     [0,0,9]]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
