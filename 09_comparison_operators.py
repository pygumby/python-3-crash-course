lang = "Python 3"

if lang == "Ruby":
    print("You're using Ruby.")
elif lang == "Python 2":
    print("Omg, please upgrade, bye.")
else:
    print(f"Anything else. The value was '{lang}'.")

age = 20

if age == 20:
    print("It's nice being 20.")
if age >= 10:
    print("You're older than 10.")
if age >= 30:
    print("You're older than 30.")
if age != 30:
    print("You're not exactly 30.")

total = None

print(type(total))

if total is None:
    print("total is None.")
