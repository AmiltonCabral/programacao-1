import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global filtra_divisores
        undertest = __import__(module)
        filtra_divisores = getattr(undertest, 'filtra_divisores', None)

    def test_exemplo(self):
        lista1 = [333, 121, 81]
        assert filtra_divisores(lista1) == None
        assert lista1 == [333,81]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
