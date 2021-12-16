import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
distribui_alunos = getattr(undertest, 'distribui_alunos', None)

class PublicTests(unittest.TestCase):

    def test_semelhante_ao_da_prova_esq(self):
        t1 = [10,38,87,22,25]
        t2 = [43,21,96,33,85,17,94]
        assert distribui_alunos(t1, t2, 6) == [[10, 43, 38, 21, 87, 96], [22, 33, 25, 85, 17, 94]]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
