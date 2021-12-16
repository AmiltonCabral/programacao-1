import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global eh_roteiro
        undertest = __import__(module)
        eh_roteiro = getattr(undertest, 'eh_roteiro', None)

    def teste_exemplo(self):
        iata = {"Campina Grande": "CPV",
               "Recife": "REC",
               "Salvador": "SSA",
               "Brasilia": "BSB",
               "Sao Paulo": "GRU",
               "Rio de Janeiro": "GIG"}


        voos = {"CPV": ["REC", "SSA"],
               "REC": ["CPV", "BSB", "GRU", "GIG"],
               "SSA": ["REC", "GRU", "GIG"],
               "BSB": ["CPV", "GIG", "GRU"],
               "GRU": ["GIG", "BSB"],
               "GIG": ["GRU", "REC"]}


        assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
        assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
        assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
