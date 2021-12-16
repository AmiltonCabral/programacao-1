import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
coluna = getattr(undertest, 'coluna', None)

class PublicTests(unittest.TestCase):

    def test_1(self):
        M = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
        assert coluna(M,0) == [1,2,3]
        assert coluna(M,1) == [1,2,3]
        assert coluna(M,2) == [1,2,3]
        assert coluna(M,3) == [1,2,3]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
