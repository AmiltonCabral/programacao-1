import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_palavras_com_mais_vogais
        undertest = __import__(module)
        remove_palavras_com_mais_vogais = getattr(undertest, 'remove_palavras_com_mais_vogais', None)

    def test_mais_de_uma(self):
        lista1 = ['arara', 'tv',   'bacia']
        assert remove_palavras_com_mais_vogais(lista1) == None
        assert lista1 == ['tv']
 
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
