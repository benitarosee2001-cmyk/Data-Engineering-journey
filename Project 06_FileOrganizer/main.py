import os
import shutil


def get_category(extension):

    if extension == [".jpg", ".png"]:
        return "Images"

    elif extension == ".mp4":
        return "Videos"

    elif extension == ".mp3":
        return "Music"

    elif extension == [".txt", ".pdf", ".docx"]:
        return "Documents"

    elif extension == ".py":
        return "Python"

    elif extension == ".zip":
        return "Archives"

    else:
        return "Others"

folder = os.path.join(os.path.dirname(__file__), "TestFolder")

files = os.listdir(folder)

for file in files:

    source = os.path.join(folder, file)

    if not os.path.isfile(os.path.join(folder, file)):
        continue

    extension = os.path.splitext(file)[1].lower()

    category = get_category(extension)

    category_folder = os.path.join(folder, category)

    os.makedirs(category_folder, exist_ok=True)

    source =os.path.join(folder, file)

    destination = os.path.join(category_folder, file)

    if os.path.exists(destination):
        print(f"Skipped: {file} already exists.")
        continue

    shutil.move(source, destination)

    print(f"{file} -> {category}")