import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global quantidade_usuarios
        undertest = __import__(module)
        quantidade_usuarios = getattr(undertest, 'quantidade_usuarios', None)
 
    def test_example(self):

        lsd = {1234:['Andrey'], 1226:['Nazareno', 'Livia'], 9999:['administrador'] }
        deq = {1114:['Ana'] }

        assert quantidade_usuarios(lsd) == 3
        assert quantidade_usuarios(deq) == 1

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
