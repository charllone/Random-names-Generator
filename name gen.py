import random

# Load names from text files
with open("first_names.txt", "r", encoding="utf-8") as f:
    first_names = [line.strip() for line in f if line.strip()]

with open("last_names.txt", "r", encoding="utf-8") as f:
    last_names = [line.strip() for line in f if line.strip()]

# Generate all possible combinations
all_combinations = [f"{first} {last}" for first in first_names for last in last_names]
random.shuffle(all_combinations)

# Number of unique names you want to generate (adjust as needed)
number_of_names = 1000  # or len(all_combinations) for all

# Take the first N unique names
unique_names = all_combinations[:number_of_names]

# Print or save to file
for name in unique_names:
    print(name)

# Ask user if they want to save
save = input("\nDo you want to save these names to a TXT file? (yes/no): ").strip().lower()

if save in ["yes", "y"]:
    filename = input("Enter a filename (without .txt): ").strip()
    with open(filename + ".txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_names))
    print(f"{number_of_names} unique names saved to {filename}.txt.")
else:
    print("Names were not saved.")