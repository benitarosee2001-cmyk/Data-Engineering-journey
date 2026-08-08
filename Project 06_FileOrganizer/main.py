import os

folder = os.path.join(os.path.dirname(__file__), "TestFolder")

files = os.listdir(folder)

for file in files:
    name, extension = os.path.splitext(file)

    if extension in [".jpg", ".png"]:
        category = "Images"

    elif extension in ".mp4":
        category = "Videos"

    elif extension in ".mp3":
        category = "Music"

    elif extension in [".txt", ".pdf", "docx"]:
        category = "Documents"

    elif extension in ".py":
        category = "Python"

    elif extension in ".zip":
        category = "Archives"

    else:
        category = "Others"

    print(f"{file} -> {category}")