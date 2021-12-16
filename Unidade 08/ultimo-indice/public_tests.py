import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
ultimo_indice = getattr(undertest, 'ultimo_indice', None)

class PublicTests(unittest.TestCase):

   def test_1(self):
      assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
      assert ultimo_indice(42, [15,2,13,11,14,2]) == -1
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
