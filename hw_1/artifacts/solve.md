## Примеры работы

Тесты:
```shell
(env) ➜  hw_1 git:(main) ✗ pytest -rpP
================================================== test session starts ==================================================
platform darwin -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/aleksejlimonov/Documents/University/itmo/mhs-python/hw_1
collected 7 items                                                                                                       

test_nl_clone.py ..                                                                                               [ 28%]
test_tail_clone.py ..                                                                                             [ 57%]
test_wc_clone.py ...                                                                                              [100%]

======================================================== PASSES =========================================================
================================================ short test summary info ================================================
PASSED test_nl_clone.py::test_nl_with_file
PASSED test_nl_clone.py::test_nl_with_stdin
PASSED test_tail_clone.py::test_tail_with_multuple_files
PASSED test_tail_clone.py::test_tail_with_stdin
PASSED test_wc_clone.py::test_wc_with_multuple_files
PASSED test_wc_clone.py::test_wc_with_single_file
PASSED test_wc_clone.py::test_wc_with_stdin
=================================================== 7 passed in 0.03s ===================================================
```

### 1.1 nl
```shell
(env) ➜  hw_1 git:(main) ✗ python3 nl_clone.py nl_clone.py
1       import sys
2
3
4       def nl():
5           input_lines = (
6               sys.stdin.readlines() if len(sys.argv) == 1 else open(sys.argv[1]).readlines()
7           )
8           for idx, line in enumerate(input_lines, start=1):
9               print(f"{idx}\t{line}", end="")
10
11
12      if __name__ == "__main__":
13          nl()
```

### 1.2 tail
```shell
(env) ➜  hw_1 git:(main) ✗ python3 tail_clone.py test_tail_clone.py

def test_tail_with_stdin(capsys):
    with patch.object(sys, "argv", ["tail_clone.py"]):
        with patch.object(sys, "stdin", io.StringIO("\n".join(map(str, range(30))))):

            tail()

            captured = capsys.readouterr().out.splitlines()
            assert len(captured) == 17
            assert captured == list(map(str, range(13, 30)))
```

### 1.3 wc
```shell
(env) ➜  hw_1 git:(main) ✗ python3 wc_clone.py wc_clone.py nl_clone.py tail_clone.py
      38     101    1035 wc_clone.py
      13      28     268 nl_clone.py
      28      61     677 tail_clone.py
      79     190    1980 total
```
