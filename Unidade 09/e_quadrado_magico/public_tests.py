# coding: utf-8
import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global eh_quadrado_magico
        undertest = __import__(module)
        eh_quadrado_magico = getattr(undertest, 'eh_quadrado_magico', None)
    
    def test_1(self):
        assert eh_quadrado_magico([[2,7,6],[9,5,1],[4,3,8]])

    def test_2(self):
        assert not eh_quadrado_magico([[1,2,3],[4,5,6]])

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
