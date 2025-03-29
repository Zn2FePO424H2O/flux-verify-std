import re

def extract_error_lines(log_file):
    pattern = re.compile(r'^error\[E0999\]: assignment might be unsafe')
    error_lines = []

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines) - 1):
                if pattern.match(lines[i].strip()):
                    error_lines.append(lines[i + 1].strip())

        for line in sorted(error_lines):
            print(line)

    except (UnicodeDecodeError, IOError):
        print(f"无法读取文件: {log_file}")

if __name__ == "__main__":
    extract_error_lines("log.txt")
