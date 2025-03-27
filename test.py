import os
import re

def search_flux_trusted(directory):
    pattern_trusted = re.compile(r'^\s*(#\[flux_attrs::trusted\])')
    pattern_verify = re.compile(r'^\s*// flux_verify.*')
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i in range(len(lines)):
                        match = pattern_trusted.match(lines[i])
                        if match and (i == 0 or not pattern_verify.match(lines[i - 1])):
                            col = match.start(1) + 1
                            print(f"{file_path}:{i + 1}:{col}")
            except (UnicodeDecodeError, IOError):
                continue

if __name__ == "__main__":
    search_flux_trusted("./library")
