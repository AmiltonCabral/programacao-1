import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_mantem_modifica
        undertest = __import__(module)
        remove_mantem_modifica = getattr(undertest, 'remove_mantem_modifica', None)

    def test_exemplo(self):
        l1 = [1, 2, 3, 120, 24]
        assert  remove_mantem_modifica(l1) == None
        assert l1 == [1, 2, 60, 12]

    def test_exemplo2(self):
        l2 = [10, 20, 24, 31]
        assert remove_mantem_modifica(l2) == None
        assert l2 == [20, 12, 31]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
