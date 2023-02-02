groceries = ["Milk", "Eggs", "Ice cream"]

for item in groceries:
    print(f"The item is '{item}'.")

name = " Python 3 Crash Course"
name = name.strip()

for char in name:
    c = char.lower()
    if c in "aeiouy":
        print(f"Vowel is '{c}'.")
        continue
    if c == "3":
        print("Breaking on '3'.")
        break
