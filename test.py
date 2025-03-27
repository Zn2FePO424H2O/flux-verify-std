import re

def extract_error_lines(log_file):
    pattern = re.compile(r'^error\[E0999\]: refinement')

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines) - 1):
                if pattern.match(lines[i].strip()):
                    print(lines[i + 1].strip())
    except (UnicodeDecodeError, IOError):
        print(f"无法读取文件: {log_file}")

if __name__ == "__main__":
    extract_error_lines("log.txt")
    