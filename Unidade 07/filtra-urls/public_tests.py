import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class AcceptanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global filtra_urls
        undertest = __import__(module)
        filtra_urls = getattr(undertest, 'filtra_urls', None)

    def test_exemplo(self):
        p1 = ['www.uol.com','www.google.com','http://mail.google.com']
        assert filtra_urls(p1) == ['www.google.com','http://mail.google.com']

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
