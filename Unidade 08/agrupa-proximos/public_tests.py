import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
agrupa_proximos = getattr(undertest, 'agrupa_proximos', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
       l = [1,2,3,4,8,22,3,5]
       assert agrupa_proximos(l,4,2) == [3,4,3,5]
       assert l == [1,2,3,4,8,22,3,5]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
