import io
import sys
import subprocess

from tempfile import NamedTemporaryFile
from wc_clone import wc
from unittest.mock import patch


def test_wc_with_multuple_files(capsys):
    with NamedTemporaryFile() as f1, NamedTemporaryFile() as f2, NamedTemporaryFile() as f3, patch.object(
        sys, "argv", ["wc_clone.py", f1.name, f2.name, f3.name]
    ):
        for i, f in enumerate([f1, f2, f3]):
            f.write("\n".join(map(str, range(30 + i * 10))).encode())
            f.flush()

        wc_args = ["wc", *sys.argv[1:]]
        out = subprocess.run(wc_args, check=True, capture_output=True)

        wc()

        captured = capsys.readouterr().out
        assert captured == out.stdout.decode()


def test_wc_with_single_file(capsys):
    with NamedTemporaryFile() as f, patch.object(sys, "argv", ["wc_clone.py", f.name]):
        f.write("\n".join(map(str, range(30))).encode())
        f.flush()

        wc_args = ["wc", *sys.argv[1:]]
        out = subprocess.run(wc_args, check=True, capture_output=True)

        wc()

        captured = capsys.readouterr().out
        assert captured == out.stdout.decode()


def test_wc_with_stdin(capsys):
    with patch.object(sys, "argv", ["wc_clone.py"]):
        wc_in = "\nabba\nabba\nabba\n\n"
        with patch.object(sys, "stdin", io.StringIO(wc_in)):

            wc()

            captured = capsys.readouterr().out
            assert captured == "%8d%8d%8d\n" % (5, 3, 17)
