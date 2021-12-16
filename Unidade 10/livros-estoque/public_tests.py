import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        global ausentes
        undertest = __import__(module)
        ausentes = getattr(undertest, 'ausentes', None)
    
    def test_exemplo(self):
        livros = { "Metamorfose": 30, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
        assert ausentes(livros) == 2

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
