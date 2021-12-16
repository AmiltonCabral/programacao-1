import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_menores
        undertest = __import__(module)
        remove_menores = getattr(undertest, 'remove_menores', None)

    def test_exemplo(self):
        lista = [1, 2, 3, 4, 5]
        assert remove_menores(3, lista) == 2
        assert lista == [3, 4, 5]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
