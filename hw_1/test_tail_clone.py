import io
import sys

from tempfile import NamedTemporaryFile
from tail_clone import tail
from unittest.mock import patch


def test_tail_with_multuple_files(capsys):

    with NamedTemporaryFile() as f1, NamedTemporaryFile() as f2, NamedTemporaryFile() as f3, patch.object(
        sys, "argv", ["tail_clone.py", f1.name, f2.name, f3.name]
    ):
        for f in [f1, f2, f3]:
            f.write("\n".join(map(str, range(30))).encode())
            f.flush()

        tail()

        captured = capsys.readouterr().out.splitlines()

        assert len(captured) == len([f1, f2, f3]) * 11
        for i, f in enumerate([f1, f2, f3]):
            assert captured[i + 10 * i] == "==> {} <==".format(f.name)
            assert captured[i * 10 + 1 + i : i * 10 + 11 + i] == list(
                map(str, range(20, 30))
            )


def test_tail_with_stdin(capsys):
    with patch.object(sys, "argv", ["tail_clone.py"]):
        with patch.object(sys, "stdin", io.StringIO("\n".join(map(str, range(30))))):

            tail()

            captured = capsys.readouterr().out.splitlines()
            assert len(captured) == 17
            assert captured == list(map(str, range(13, 30)))
