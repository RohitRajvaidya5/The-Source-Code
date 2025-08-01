# Context Managers

from contextlib import contextmanager

# Best example of context managers

with open ("Test_files/file.txt", "w") as file:
    file.write("This is the contents of the file.")


# Implementation
# class OpenFile:
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#     def __enter__(self):
#         self.file = open(self.file_name, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()

@contextmanager
def open_file(files, mode):
    f = open(files, mode)
    yield f
    f.close()


with open_file("Test_files/file.txt", "w") as file:
    file.write("Implementation of context manager")

print(file.closed)
