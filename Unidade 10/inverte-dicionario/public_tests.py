import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global inverte_dicionario
        undertest = __import__(module)
        inverte_dicionario = getattr(undertest, 'inverte_dicionario', None)

    def test_exemplo(self):
        m = {"a": 2, "b": 3, "c": 2}
        assert inverte_dicionario(m) == {2: ["a", "c"],3: ["b"]}

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
