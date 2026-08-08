import os
import shutil

folder = os.path.join(os.path.dirname(__file__), "TestFolder")

files = os.listdir(folder)

for file in files:

    if not os.path.isfile(os.path.join(folder, file)):
        continue

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

    category_folder = os.path.join(folder, category)

    os.makedirs(category_folder, exist_ok=True)

    source =os.path.join(folder, file)

    destination = os.path.join(category_folder, file)

    shutil.move(source, destination)

    print(f"{file} -> {category}")