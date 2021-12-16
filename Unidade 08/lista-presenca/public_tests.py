import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global cria_lista_presenca
        undertest = __import__(module)
        cria_lista_presenca = getattr(undertest, 'cria_lista_presenca', None)

    def test_exemplo(self):
        turmas = [1, 2, 2, 4, 5, 3, 5]
        nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
        assert cria_lista_presenca(turmas, nomes, 5) == ["Carla", "Jose"]
        assert turmas == [1, 2, 2, 4, 5, 3, 5]
        assert nomes == ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
