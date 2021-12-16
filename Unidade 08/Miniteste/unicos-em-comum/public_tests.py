import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global unicos_em_comum
        undertest = __import__(module)
        unicos_em_comum = getattr(undertest, 'unicos_em_comum', None)

    def test_exemplo1(self):
        l1 = [ 'A', 'A', 'B', 'C', 'C']
        l2 = ['B', 'A']
        assert unicos_em_comum(l1, l2) == ['B']

    def test_exemplo2(self):
        l1 = ['A', 'A', 'B', 'C']
        l2 = ['A', 'B', 'C']
        assert unicos_em_comum(l1, l2) == ['B', 'C']

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
