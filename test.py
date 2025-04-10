import os
import re

def find_flux_verify_error_trusted_lines(directory):
    error_pattern = re.compile(r'^\s*//\s*flux_verify_error:(?!.*(?:complex|refinement type error|logic constraint)).*$')
    trusted_pattern = re.compile(r'^\s*#\[flux_attrs::trusted.*\].*$')

    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith('.rs'):
                continue

            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()

            for i in range(len(lines) - 1):
                if error_pattern.match(lines[i]):
                    next_line = lines[i + 1]
                    if trusted_pattern.match(next_line):
                        col_num = len(next_line) - len(next_line.lstrip()) + 1
                        results.append(f"{file_path}:{i + 2}:{col_num}: Found `#flux_attrs::trusted` after `// flux_verify_error:`")

    if results:
        print("\n".join(results))
    else:
        print("No matches found.")

find_flux_verify_error_trusted_lines('./library')
