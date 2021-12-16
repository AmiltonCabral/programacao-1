import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class AcceptanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global filtra_lista
        undertest = __import__(module)
        filtra_lista = getattr(undertest, 'filtra_lista', None)

    def test_1(self):
        lista1 = list(range(10))
        assert filtra_lista(2, lista1) == [0,2,4,6,8]
        assert filtra_lista(3, lista1) == [0,3,6,9]
        assert lista1 == list(range(10))

    def test_2(self):
        lista2 = [2,3,5,7,11,13,17]
        assert filtra_lista(4, lista2) == [2,11]
        assert filtra_lista(40, lista2) == [2]
        assert lista2 == [2,3,5,7,11,13,17]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
