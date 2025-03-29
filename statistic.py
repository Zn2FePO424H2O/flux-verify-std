import os
import re
from collections import defaultdict

def find_flux_verify_tags(root_dir):
    pattern = re.compile(r'^\s*// flux_verify_([\w]+):\s*(.+)$')
    tag_counts = defaultdict(int)
    tag_details = defaultdict(lambda: defaultdict(int))
    tag_locations = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, start=1):
                        match = pattern.match(line)
                        if match:
                            tag1, tag2 = match.groups()
                            tag_counts[tag1] += 1
                            tag_details[tag1][tag2] += 1
                            tag_locations[tag1].append((file_path, line_number))
            except (UnicodeDecodeError, IOError):
                continue

    return tag_counts, tag_details, tag_locations

if __name__ == "__main__":
    search_directory = "./library"
    tag_counts, tag_details, tag_locations = find_flux_verify_tags(search_directory)

    for tag1 in sorted(tag_counts.keys()):
        if tag1 == "mark":
            continue
        print(f"{tag1}: {tag_counts[tag1]}")
        for tag2, count in sorted(tag_details[tag1].items()):
            print(f"  - {tag2}: {count}")
