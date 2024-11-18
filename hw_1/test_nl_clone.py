import io
import sys

from tempfile import NamedTemporaryFile
from nl_clone import nl
from unittest.mock import patch


def test_nl_with_file(capsys):
    with NamedTemporaryFile() as f:
        with patch.object(sys, "argv", ["nl_clone.py", f.name]):
            f.write(b"line1\nline2\nline3\n")
            f.flush()

            nl()

            captured = capsys.readouterr()
            assert captured.out == "1\tline1\n2\tline2\n3\tline3\n"


def test_nl_with_stdin(capsys):
    with patch.object(sys, "argv", ["nl_clone.py"]):
        with patch.object(sys, "stdin", io.StringIO("line1\nline2\nline3\n")):

            nl()

            captured = capsys.readouterr()
            assert captured.out == "1\tline1\n2\tline2\n3\tline3\n"
