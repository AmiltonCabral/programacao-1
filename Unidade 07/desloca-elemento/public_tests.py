import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
desloca = getattr(undertest, 'desloca', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
  
        l1 = [2,6,9,11,13,5]
        desloca(l1, 2, 4)
        assert l1 == [2,6,11,13,9,5]

    def test_exemplo2(self):
        l1 = [0,1,2,3,4,5,6]
        desloca(l1, 4, 6)
        assert l1 == [0,1,2,3,5,6,4]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
