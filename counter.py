from collections import Counter

error_counts = Counter()
capture = False
filtered_lines = []
e0999_count = 0
other_error_count = 0
last_non_empty_line = ""

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        stripped_line = line.strip()
        if stripped_line:
            last_non_empty_line = stripped_line

        if stripped_line.startswith("error[E0999]:"):
            error_counts[stripped_line] += 1
            e0999_count += 1
            capture = True
        elif stripped_line.startswith("error: ") and not stripped_line.startswith("error: could not compile"):
            parts = stripped_line.split(":")
            error_counts[":".join(parts[:2] + parts[5:])] += 1
            other_error_count += 1
            capture = False
        if capture:
            filtered_lines.append(line)

with open("log[E0999].txt", "w", encoding="utf-8") as filtered_file:
    filtered_file.writelines(filtered_lines)

print("--start of errors--\n")

print("Other errors:")
for error in sorted(error_counts):
    if not error.startswith("error[E0999]:"):
        print(f"{error} -> {error_counts[error]}")
print(f"\nTotal other errors: {other_error_count}\n")

print("Errors of type error[E0999]:")
for error in sorted(error_counts):
    if error.startswith("error[E0999]:"):
        print(f"{error} -> {error_counts[error]}")
print(f"\nTotal error[E0999]: {e0999_count}\n")

print("--end of errors--\n")

if last_non_empty_line.startswith("error: could not compile") and "previous errors" in last_non_empty_line:
    print("Warning: The compilation process was not completed successfully. Some errors may not be fully captured.\n")
