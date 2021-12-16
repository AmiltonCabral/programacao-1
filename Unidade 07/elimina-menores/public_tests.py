import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
elimina_menores = getattr(undertest, 'elimina_menores', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        lista1 = [100,200,300,400]
        assert elimina_menores(100, lista1) == 0
        assert lista1 == [100,200,300,400]
        
    def test_exemplo_2(self):
        lista2 = [3,5,1,7,10,9]
        assert elimina_menores(4, lista2) == 2
        assert lista2 == [5,7,10,9]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
