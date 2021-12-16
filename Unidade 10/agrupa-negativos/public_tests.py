import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global agrupa_negativos
        undertest = __import__(module)
        agrupa_negativos = getattr(undertest, 'agrupa_negativos', None)

    def test_example(self):
        assert agrupa_negativos([10, -2, -7, 8]) == {"nao-negativos":[10, 8], "negativos":[-2,-7]}
        assert agrupa_negativos([-1, -5]) == {"nao-negativos":[ ], "negativos":[-1, -5]}

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
