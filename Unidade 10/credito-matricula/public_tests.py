# coding: utf-8
import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global num_creditos
        undertest = __import__(module)
        num_creditos = getattr(undertest, 'num_creditos', None)
    
    def test_1(self):
       bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]}, "UAF": {("Física Clássica", 4): ["11624200"], ("Física Moderna", 4): ["11624300", "11624500", "11624600"]}, "UAM": {("Cálculo I", 4): ["11624100", "11624300"], ("Álgebra Linear", 4): ["11624300"]}}
        
       assert num_creditos(bd_ufcg, "11624100") == 8

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
