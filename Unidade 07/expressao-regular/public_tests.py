import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
is_substring_expr = getattr(undertest, 'is_substring_expr', None)

class PublicTests(unittest.TestCase):

    def test_1(self):
        assert is_substring_expr('oicarovoce','oi*voce')
        assert is_substring_expr('oicvoce','oi*voce')

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
