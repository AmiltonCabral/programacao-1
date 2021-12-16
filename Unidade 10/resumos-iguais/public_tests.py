import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global agrupa_resumos_iguais
        undertest = __import__(module)
        agrupa_resumos_iguais = getattr(undertest, 'agrupa_resumos_iguais', None)
 
    def test_1_caso_base(self):
        lista1 = [20000, 3435, 159, 200, 2] 
        self.assertEqual(agrupa_resumos_iguais(lista1), {2:[20000, 200, 2], 15:[3435,159]})

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
