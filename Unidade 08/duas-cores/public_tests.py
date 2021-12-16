import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
separa_duas_cores = getattr(undertest, 'separa_duas_cores', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = ['a', 'a', 'b', 'a', 'b']
        assert separa_duas_cores(l1, 'b', 'a') == None
        assert l1 == [ 'b', 'b', 'a', 'a', 'a']
     
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
