import os
import re
import csv
from collections import defaultdict

def find_flux_verify_tags(root_dir):
    pattern = re.compile(r'^\s*// flux_verify_([\w]+):\s*(.+)$')
    tag_counts = defaultdict(int)
    tag_details = defaultdict(lambda: defaultdict(int))
    tag_locations = defaultdict(list)
    file_error_details = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    error_links = defaultdict(lambda: defaultdict(str))

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
                            file_error_details[file_path][tag1][tag2] += 1
                            if not error_links[tag1][tag2]:
                                error_links[tag1][tag2] = f"{file_path}#L{line_number}"
            except (UnicodeDecodeError, IOError):
                continue

    return tag_counts, tag_details, tag_locations, file_error_details, error_links

def generate_csv(file_error_details, tag_details, error_links, output_path="count.csv"):
    # Categories: panic, ice, and refinement_error (error + complex)
    categories = {
        "panic": sorted(tag_details.get("panic", {}).keys()),
        "ice": sorted(tag_details.get("ice", {}).keys()),
        "refinement_error": sorted(tag_details.get("error", {}).keys()) + sorted(tag_details.get("complex", {}).keys())
    }

    # Headers for the CSV file
    headers = ["file", "panic_total", "ice_total", "refinement_error_total"]
    link_row = ["", "", "", ""]

    # Add category-specific columns
    for cat in ["panic", "ice", "refinement_error"]:
        headers += [f"{cat}_{e}" for e in categories[cat]]
        link_row += [error_links[cat].get(e, "") for e in categories[cat]]

    # Prepare the data rows
    data_rows = []
    for file_path, cat_data in file_error_details.items():
        # Calculate total errors for each category
        panic_total = sum(cat_data.get("panic", {}).values())
        ice_total = sum(cat_data.get("ice", {}).values())
        refinement_error_total = sum(cat_data.get("error", {}).values()) + sum(cat_data.get("complex", {}).values())

        total_sum = panic_total + ice_total + refinement_error_total
        if total_sum == 0:
            continue

        # Row starts with file path and total sum of each category
        row = [file_path, panic_total, ice_total, refinement_error_total]

        # Add counts for each category's error types
        for cat in ["panic", "ice", "refinement_error"]:
            row += [cat_data.get(cat, {}).get(e, 0) for e in categories[cat]]

        # Determine if it's a row with 0 panic and 0 ice but refinement errors
        is_refinement_first = (panic_total == 0 and ice_total == 0 and refinement_error_total > 0)

        data_rows.append((is_refinement_first, total_sum, row))

    # Sort rows:
    # - First by rows that have 0 panic and 0 ice, but have refinement errors
    # - Then by total_sum (panic_total + ice_total + refinement_error_total)
    data_rows.sort(key=lambda x: (not x[0], x[1]))

    # Write to CSV file
    with open(output_path, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(link_row)
        for _, _, row in data_rows:
            writer.writerow(row)

if __name__ == "__main__":
    search_directory = "./library"
    tag_counts, tag_details, tag_locations, file_error_details, error_links = find_flux_verify_tags(search_directory)

    for tag1 in sorted(tag_counts.keys()):
        if tag1 == "mark":
            continue
        print(f"{tag1}: {tag_counts[tag1]}")
        for tag2, count in sorted(tag_details[tag1].items()):
            print(f"  - {tag2}: {count}")

    generate_csv(file_error_details, tag_details, error_links)
