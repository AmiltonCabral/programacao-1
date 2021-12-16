import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global is_substring
        undertest = __import__(module)
        is_substring = getattr(undertest, 'is_substring', None)

    def test_1(self):
        assert is_substring('boiada','oi')
        assert not is_substring('casorio', 'casa')

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
