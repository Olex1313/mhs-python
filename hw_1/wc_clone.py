import sys


def wc():
    files = sys.argv[1:]
    total_lines, total_words, total_bytes = 0, 0, 0

    def count_stats(file_content):
        words = file_content.split()
        return file_content.count("\n"), len(words), len(file_content.encode())

    if not files:
        file_content = sys.stdin.read()
        lines, words, bytes_ = count_stats(file_content)
        print("%8d%8d%8d" % (lines, words, bytes_))
        return

    for file_name in files:
        try:
            with open(file_name, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"wc: cannot open '{file_name}' for reading: No such file")
            continue

        lines, words, bytes_ = count_stats(content)
        total_lines += lines
        total_words += words
        total_bytes += bytes_

        print("%8d%8d%8d %s" % (lines, words, bytes_, file_name))

    if len(files) > 1:
        print("%8d%8d%8d total" % (total_lines, total_words, total_bytes))


if __name__ == "__main__":
    wc()
