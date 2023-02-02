with open("08_new_file.py", "w") as file_handler:
    file_handler.write("print('Hello, world.')")
    file_handler.close()

with open("08_new_file.py", "a") as fh:
    fh.write("\nprint('Second line')")
    fh.close()

with open("08_new_file.py", "r") as fh:
    content = fh.read()
    fh.close()

print(content)
