import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
insere_ordenado_ultimo = getattr(undertest, 'insere_ordenado_ultimo', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = [2,6,9,11,13,5]
        insere_ordenado_ultimo(l1)
        assert l1 == [2,5,6,9,11,13]
    
    def test_outro(self):
        l2 = [1,2,3,0]
        insere_ordenado_ultimo(l2)
        assert l2 == [0,1,2,3]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
