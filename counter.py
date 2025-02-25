from collections import Counter

error_counts = Counter()

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("error[E0999]:"):
            error_counts[line.strip()] += 1
        elif line.startswith("error: ") and not line.startswith("error: could not compile"):
            parts = line.strip().split(":")
            error_counts[":".join(parts[:2] + parts[5:])] += 1

print("--start of errors--")
for error in sorted(error_counts):
    print(f"{error} -> {error_counts[error]}")
print("--end of errors--")