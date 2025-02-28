import re
import argparse

parser = argparse.ArgumentParser(description="Convert CubyMark to TailwindCSS HTML")

parser.add_argument("-i", "--input", required=True, help="Input CubyMark file")
parser.add_argument("-o", "--output", required=True, help="Output TailwindCSS HTML file")

args = parser.parse_args()

with open(args.input, "r") as f:
    input_text = f.read()

