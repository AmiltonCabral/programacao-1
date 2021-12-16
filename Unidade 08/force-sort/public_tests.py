import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
force_sort = getattr(undertest, 'force_sort', None)

class PublicTests(unittest.TestCase):

   def test_exemplo_1(self):
      seq = [1, 3, 5, 4, 9]
      assert force_sort(seq) == [0, 0, 0, 1, 0]

   def test_exemplo_2(self):
      seq = [1, 3, 5, 4, 9, 2, 15]
      assert force_sort(seq) == [0, 0, 0, 1, 0, 7, 0]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
