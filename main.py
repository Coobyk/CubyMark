def convert(input_file, output_file):
    with open(input_file, "r") as f:
        content = f.read()
    
    print(content)

    with open(output_file, "w") as f:
        f.write(content)

if (__name__ == "__main__"):
    convert("input.cum", "output.html")