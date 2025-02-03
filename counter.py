from collections import Counter

error_counts = Counter()

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("error[E0999]:"):
            error_counts[line.strip()] += 1

for error in sorted(error_counts):
    print(f"{error} -> {error_counts[error]}")
