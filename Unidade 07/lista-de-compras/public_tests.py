import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global adiciona_item
        undertest = __import__(module)
        adiciona_item = getattr(undertest, 'adiciona_item', None)

    def test_exemplo(self):
       lista = ['acucar', 'leite', 'paes', 'queijo']
       adiciona_item('cafe', lista)
       assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']
        

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
