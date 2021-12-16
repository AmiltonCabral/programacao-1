import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filtra_alunos = getattr(undertest, 'filtra_alunos', None)

class PublicTests(unittest.TestCase):

    def test_1(self):
        inscritos = [121, 123, 124]
        alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
        assert filtra_alunos(alunos, inscritos, 7.0) == 4
        assert alunos == [ (121,7.5), (124,9.0) ]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
