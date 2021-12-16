import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
merge_invertido = getattr(undertest, 'merge_invertido', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = [8, 12, 78, 79, 511]
        l2 = [7, 8, 121, 302]
        assert merge_invertido(l1, l2) == [511, 302, 121, 79, 78, 12, 8, 8, 7]
        assert l1 == [8, 12, 78, 79, 511]
        assert l2 == [7, 8, 121, 302]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
