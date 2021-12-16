import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global consulta_direita
        undertest = __import__(module)
        consulta_direita = getattr(undertest, 'consulta_direita', None)

    def test_1(self):
        labirinto1 = [
          ['P', '*', ' ', ' '],
          ['P', ' ', 'P', ' '],
          ['P', 'P', 'P', ' '],
        ]

        assert consulta_direita(labirinto1) == 2

    def test_2(self):
        labirinto2 = [
          ['P', 'P', ' ', ' '],
          ['P', '*', 'P', ' '],
          ['P', 'P', 'P', ' '],
        ]

        assert consulta_direita(labirinto2) == 0

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
