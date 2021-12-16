import unittest
import sys

module  = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global ordena_vpb
        undertest = __import__(module)
        ordena_vpb = getattr(undertest, 'ordena_vpb', None)

    def test_basico(self):
        l = ['b', 'v', 'v', 'p', 'b', 'v', 'b']
        assert ordena_vpb(l) == None
        assert l == ['v', 'v', 'v', 'p', 'b', 'b', 'b']


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
