try:
    1 / 0
    print("Show me!")
except Exception as e: # alternatively: `except ZeroDivisionError`
    print(e)
    print(type(e))

print("This still runs!")
