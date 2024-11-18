import sys


def nl():
    input_lines = (
        sys.stdin.readlines() if len(sys.argv) == 1 else open(sys.argv[1]).readlines()
    )
    for idx, line in enumerate(input_lines, start=1):
        print(f"{idx}\t{line}", end="")


if __name__ == "__main__":
    nl()
