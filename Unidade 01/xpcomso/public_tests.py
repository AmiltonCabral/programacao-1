import unittest
import sys
import mimetypes
import subprocess
import string

arquivo = sys.argv[-1]
module = arquivo.split(".py")[0]
mimetype = subprocess.check_output(['file', '--mime-type', arquivo]).decode().split(':', 1)[1].strip()
encoding = subprocess.check_output(['file', '--mime-encoding', arquivo]).decode().split(':', 1)[1].strip()


def is_posix_filename(name, extra_chars=""):
    CHARS = string.ascii_letters + string.digits + "._-" + extra_chars
    return all(c in CHARS for c in name)


class PublicTests(unittest.TestCase):

    def test_nome_do_arquivo(self):
        assert is_posix_filename(arquivo), "nome de arquivo inválido"

    def test_conteudo_do_arquivo(self):
        assert mimetype.startswith('text/'), "conteúdo/mimetype inválido"

    def test_encoding(self):
        ACEITAVEIS = ["utf-8", "latin1", "us-ascii", "ascii"]
        assert encoding in ACEITAVEIS, "encoding inválido"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
