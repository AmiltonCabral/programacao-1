import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global senha
        undertest = __import__(module)
        senha = getattr(undertest, 'senha', None)

    def test_exemplo(self):
        splab = {1313:['Franklin', 'Jorge'], 1226:['Eliane', 'Dalton'], 1507:['Wilkerson'] }
        assert senha(splab, 'Franklin') == 1313

    def test_exemplo2(self):
        splab = {1313:['Franklin', 'Jorge'], 1226:['Eliane', 'Dalton'], 1507:['Wilkerson'] }
        assert senha(splab, 'Matheus') == -1


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
