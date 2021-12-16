import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global concatena_simetricos
        undertest = __import__(module)
        concatena_simetricos = getattr(undertest, 'concatena_simetricos', None)

    def test_exemplo_1(self):
        assert concatena_simetricos(["bola", "tv", "zebra", "arara"]) == ["ararabola", "tvzebra"]

    def test_exmplo_2(self):
        assert concatena_simetricos(["ab", "cd", "ef", "gh", "ij"]) == ["abij", "cdgh", "ef"]

    def test_exemplo_3(self):
        assert concatena_simetricos(["cd", "gh", "ck"]) == ["cdck", "gh"]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
