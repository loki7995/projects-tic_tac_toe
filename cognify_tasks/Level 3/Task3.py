import os
import shutil

# Path to the folder to organize
SOURCE_FOLDER = "files_to_organize"

# File type categories
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"]
}

def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Source folder does not exist.")
        return

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    dest_folder = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(SOURCE_FOLDER, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

    print("Files organized successfully.")

# Run automation
organize_files()
