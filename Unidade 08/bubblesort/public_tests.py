import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
bubblesort = getattr(undertest, 'bubblesort', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        lista = [3,9,1,2]
        bubblesort(lista)
        assert lista == [1,2,3,9]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
