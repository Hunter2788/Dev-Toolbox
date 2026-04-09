import os
import shutil

def run():
    path = input("Enter folder path: ")

    if not os.path.exists(path):
        print("Folder not found")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1].lower()

            if ext in ["jpg", "png", "gif"]:
                folder = "Images"
            elif ext in ["pdf", "docx", "txt"]:
                folder = "Documents"
            elif ext in ["mp4", "mov"]:
                folder = "Videos"
            else:
                folder = "Others"

            target_folder = os.path.join(path, folder)
            os.makedirs(target_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(target_folder, file))

    print("Files organized successfully.")
