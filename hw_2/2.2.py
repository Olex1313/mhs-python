import argparse
import subprocess
import os

from latex_generator_olex1313 import generate_latex_table, generate_latex_image


def main(image_path, output_file):
    data = [
        ["Col1", "Col2", "Col3", "Col4"],
        ["a", 1, "b", "c"],
        ["d", 2, "e", "f"],
    ]

    latex_code = generate_latex_table(data)

    latex_image = generate_latex_image(image_path=image_path)

    with open(output_file, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\begin{document}\n")
        f.write(latex_code)
        f.write(latex_image)
        f.write("\n\\end{document}")

    print(f"LaTeX file generated successfully: {output_file}")

    try:
        output_dir = os.path.dirname(output_file) or "."
        subprocess.run(
            ["pdflatex", "-output-directory", output_dir, output_file], check=True
        )
        print(f"PDF succesfully compiled and saved to {output_dir}")
    except FileNotFoundError:
        print("Error: pdflatex not found. Make sure it's installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation of LaTeX file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate LaTeX file with table and image."
    )
    parser.add_argument(
        "image_path", help="Path to the image file to include in the LaTeX document."
    )
    parser.add_argument(
        "--output",
        default="example_table.tex",
        help="Path to save the generated LaTeX file (default: example_table.tex).",
    )
    args = parser.parse_args()

    main(image_path=args.image_path, output_file=args.output)
