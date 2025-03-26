import os
import re
from collections import defaultdict

def find_flux_verify_tags(root_dir):
    pattern = re.compile(r'^\s*// flux_verify:\s*(\S+)')
    tag_counts = defaultdict(int)
    tag_locations = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, start=1):
                        match = pattern.match(line)
                        if match:
                            tag = match.group(1)
                            tag_counts[tag] += 1
                            tag_locations[tag].append((file_path, line_number))
            except (UnicodeDecodeError, IOError):
                continue

    return tag_counts, tag_locations

if __name__ == "__main__":
    search_directory = "./library/core/src"
    tag_counts, _ = find_flux_verify_tags(search_directory)

    for tag, count in sorted(tag_counts.items()):
        print(f"{tag}: {count}")
