import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global filtra_caixas_indisponiveis
        undertest = __import__(module)
        filtra_caixas_indisponiveis = getattr(undertest, 'filtra_caixas_indisponiveis', None)

    def test_basico(self):
        caixas = [0,1,2,3,4,5,6]
        filtra_caixas_indisponiveis(caixas,3)
        assert caixas == [3,4,5,6]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
