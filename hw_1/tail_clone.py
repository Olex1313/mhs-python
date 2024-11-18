import sys


def tail():
    in_files = sys.argv[1:]
    if not in_files:
        input_lines = sys.stdin.readlines()
        print("".join(input_lines[-17:]), end="")
        return

    for file_idx, file_name in enumerate(in_files):
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"tail: cannot open '{file_name}' for reading: No such file")
            continue

        if len(in_files) > 1:
            if file_idx > 0:
                print()
            print(f"==> {file_name} <==")

        print("".join(lines[-10:]), end="")


if __name__ == "__main__":
    tail()
