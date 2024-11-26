import argparse
from latex_generator_olex1313 import generate_latex_table


def main(output_file):
    data = [
        ["Col1", "Col2", "Col3", "Col4"],
        ["a", 1, "b", "c"],
        ["d", 2, "e", "f"],
    ]

    latex_code = generate_latex_table(data)

    with open(output_file, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\begin{document}\n")
        f.write(latex_code)
        f.write("\n\\end{document}")

    print(f"LaTeX file generated successfully: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate LaTeX file with table.")
    parser.add_argument(
        "--output",
        default="example_table.tex",
        help="Path to save the generated LaTeX file (default: example_table.tex).",
    )
    args = parser.parse_args()

    main(output_file=args.output)
