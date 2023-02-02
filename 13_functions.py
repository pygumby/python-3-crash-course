def name():
    return "A thing"

my_thing = name()

print(my_thing)

def greeting(name):
    print(f"{name}, hello to you, good sir.")

greet = greeting("Zephyr")

print(type(greet))

def greeting2(name, greeting = "hello"):
    return f"{name}, {greeting} to you."

greet2 = greeting2("Henry")

print(greet2)
print(type(greet2))
