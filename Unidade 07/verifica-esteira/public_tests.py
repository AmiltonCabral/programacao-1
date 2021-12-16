import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
verifica_esteira = getattr(undertest, 'verifica_esteira', None)

class PublicTests(unittest.TestCase):

    def test_example(self):
        l1 = [2,1,3,4]
        l2 = [2]
        assert verifica_esteira(l1,l2)
        assert l1 == [2,1,3,4]
        assert l2 == [2]

        l1 = [1,3,4]
        l2 = [4,1]
        assert not verifica_esteira(l1,l2)
        assert l1 == [1,3,4]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
