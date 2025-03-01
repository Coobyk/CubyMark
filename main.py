import re
import argparse

def convert_cubymark_to_html(input_text):
    # Process Headers
    html = re.sub(r"^(#+)\s+(.+)$", r"<h\1>\0</h\1>", input_text)

    # Process Paragraphs
    html = re.sub(r"(.+?)\n", r"<p>\1</p>", html)

    # Process Lists
    html = re.sub(r"^(?:- )(.+)$", r"<li>\2</li>", html)

    return html

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Convert CubyMark to TailwindCSS HTML")

    # Add input and output file arguments
    parser.add_argument("-i", "--input", type=argparse.FileType('r'), required=True, help="Input CubyMark file")
    parser.add_argument("-o", "--output", type=argparse.FileType('w'), required=True, help="Output TailwindCSS HTML file")

    # Parse the arguments
    args = parser.parse_args()

    # Read the content of the input file
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            input_text = f.read()
            if not input_text.strip():
                print("Input file is empty. Please provide a valid CubyMark file.")
                exit(1)
    except IOError as e:
        print(f"Error reading input file: {e}")
        exit(1)

    # Convert CubyMark to basic HTML
    html = convert_cubymark_to_html(input_text)

    # Write the converted HTML to the output file
    try:
        with open(args.output, "w") as f:
            f.write(html)
    except IOError:
        print(f"Error writing output file: {args.output} does not exist. Creating it.")
        with open(args.output, "x") as f:
            f.write(html)

