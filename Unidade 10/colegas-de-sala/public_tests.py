import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
colegas_de_sala = getattr(undertest, 'colegas_de_sala', None)

class PublicTests(unittest.TestCase):

    def test_example(self):

        salasprofs = {
            'Franklin': 206,    'Tiago':206,        'Eliane': 206,
            'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
            'Jorge': 204
        }

        assert set(colegas_de_sala(salasprofs, 'Franklin')) == set(['Tiago', 'Eliane'])
        assert set(colegas_de_sala(salasprofs, 'Adalberto')) == set([])
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
