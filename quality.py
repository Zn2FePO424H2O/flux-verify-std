import os
import re

def check_flux_statements(directory):
    trusted_pattern = re.compile(r'^\s*#\[flux_attrs::trusted.*\].*$')
    assume_pattern = re.compile(r'^\s*flux_assume\(.*\).*$', re.DOTALL)
    verify_pattern = re.compile(r'^\s*// flux_verify_.*$')

    violations = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(('.rs')):
                continue
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            for i in range(1, len(lines)):
                current_line = lines[i]
                prev_line = lines[i - 1].strip()
                
                if trusted_pattern.match(current_line) or assume_pattern.match(current_line):
                    if not verify_pattern.match(prev_line):
                        col_num = len(current_line) - len(current_line.lstrip()) + 1
                        violations.append(f"{file_path}:{i+1}:{col_num}: Missing required `// flux_verify_...` annotation")

    if violations:
        print("\n".join(violations))
    else:
        print("All files comply with the required format.")

# 运行检查
check_flux_statements('./library')
