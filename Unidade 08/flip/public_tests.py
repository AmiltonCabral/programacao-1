import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global flip
        undertest = __import__(module)
        flip = getattr(undertest, 'flip', None)

    def test_exemplo(self):
        l1 = [1, 2, 3, 4, 5, 6, 7]
        assert flip(l1, 2, 5) == None
        assert l1 == [1, 2, 6, 5, 4, 3, 7]
     
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
