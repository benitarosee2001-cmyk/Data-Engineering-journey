import os

folder = os.path.join(os.path.dirname(__file__), "TestFolder")

files = os.listdir(folder)

for file in files:
    name, extension = os.path.splitext(file)

    print("File: ", file)
    print("Extension: ", extension)