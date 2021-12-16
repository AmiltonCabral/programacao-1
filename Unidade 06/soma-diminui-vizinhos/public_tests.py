import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global soma_diminui_vizinhos
        undertest = __import__(module)
        soma_diminui_vizinhos = getattr(undertest, 'soma_diminui_vizinhos', None)

    def test_simples(self):
        lista = [1,2,3]
        assert soma_diminui_vizinhos(lista) == 0

    def test_vazio(self):
        lista = []
        assert soma_diminui_vizinhos(lista) == 0


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
