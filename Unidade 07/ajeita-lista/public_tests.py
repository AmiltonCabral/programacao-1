import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
ajeita_lista = getattr(undertest, 'ajeita_lista', None)

class PublicTests(unittest.TestCase):

   def test_do_enunciado(self):
       lista1 = [3,2,1,4,5,6,7,8,9]
       assert ajeita_lista(lista1) == None
       assert lista1 == [8, 6, 4, 2, 1, 3, 5, 7, 9]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
