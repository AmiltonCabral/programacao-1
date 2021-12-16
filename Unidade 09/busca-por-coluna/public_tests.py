import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
busca_todos_por_coluna_em_matriz = getattr(undertest, 'busca_todos_por_coluna_em_matriz', None)

class AcceptanceTests(unittest.TestCase):

    def test_exemplo_1(self):
        m = [ [2, 3, 5, 3, 1], [3, 2, 1, 5, 6], [3, 2, 3, 2, 1] ]
        assert busca_todos_por_coluna_em_matriz(m, 4) == []

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
