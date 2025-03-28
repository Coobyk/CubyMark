import re
import argparse
import os

def convert_cubymark_to_html(input_text):

    # Process Headers
    html = re.sub(r"^(#+)\s+(.+)$", r"<h\1>\0</h\1>", input_text)

    # Process Paragraphs
    html = re.sub(r"(.+?)\n", r"<p>\1</p>", html)

    # Process Lists
    html = re.sub(r"^(?:- )(.+)$", r"<li>\1</li>", html)

    return html

def checkfiles():
    # Check if the input file exists
    if not args.input:
        print("Input file does not exist. Please provide a valid CubyMark file.")
        exit(1)

    # Check if the input file is a CubyMark file
    if not args.input.lower().endswith(".cum"):
        print("Input file is not a CubyMark file. Please provide a valid CubyMark file.")
        exit(1)

    # Create the required directories for the output file if needed
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError as e:
            print(f"Error creating output directory: {e}")
            exit(1)
    
    # Create CSS file if needed
    if not os.path.exists("src/input.css"):
        try:
            with open("src/input.css", "w") as f:
                f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")
        except OSError as e:
            print(f"Error creating CSS file: {e}")
            exit(1)



if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Convert CubyMark to TailwindCSS HTML")

    # Add input and output file arguments
    parser.add_argument("-i", "--input", required=True, help="Input CubyMark file")
    parser.add_argument("-o", "--output", required=True, help="Output TailwindCSS HTML file")

    # Parse the arguments
    args = parser.parse_args()

    checkfiles()

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
    with open(args.output, "w") as f:
        f.write(html)

