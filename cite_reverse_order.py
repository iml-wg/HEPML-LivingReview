import re


def reverse_citations_in_tex(file_path, output_path=None):
    r"""Reverse the order of citation keys in all \cite{...} blocks in a .tex file."""

    # Read the content of the .tex file
    with open(file_path) as file:
        content = file.read()

    # Regular expression to match \cite{...} blocks
    cite_pattern = re.compile(r'\\cite\{([^}]+)\}')

    # Function to reverse the order of keys within each cite block
    def reverse_cite_keys(match):
        keys = match.group(1).split(',')
        reversed_keys = ','.join(keys[::-1])
        return f'\\cite{{{reversed_keys}}}'

    # Replace all \cite{...} blocks with reversed citation order
    updated_content = cite_pattern.sub(reverse_cite_keys, content)

    # Write the updated content back to the same file or a new file
    output_file = output_path
    with open(output_file, 'w') as file:
        file.write(updated_content)

    print(f"Updated citations saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    input_file = 'HEPML.tex'
    output_file = 'HEPML_cite_reverse.tex'
    reverse_citations_in_tex(input_file, output_file)