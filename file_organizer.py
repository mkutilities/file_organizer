import os
import shutil
import logging

logging.basicConfig(filename="logs/file_organizer.log", filemode="a",
                    level=logging.DEBUG, format="%(asctime)s - %(message)s")


def count_files_by_extension(dir_path):
    file_types = {}
    for item in os.listdir(dir_path):
        s = os.path.join(dir_path, item)
        if os.path.isfile(s):
            _, file_extension = os.path.splitext(item)
            if file_extension in file_types:
                file_types[file_extension] += 1
            else:
                file_types[file_extension] = 1
        if os.path.isdir(s):
            file_types_in_subdir = count_files_by_extension(s)
            for file_extension, count in file_types_in_subdir.items():
                if file_extension in file_types:
                    file_types[file_extension] += count
                else:
                    file_types[file_extension] = count
    return file_types


def organize_files(dir_path):
    for item in os.listdir(dir_path):
        s = os.path.join(dir_path, item)
        if os.path.isfile(s):
            if item.endswith(".py") or item.endswith(".ipynb") or item.endswith(".ipynb_checkpoints"):
                folder_name, _ = os.path.splitext(item)
                folder_path = os.path.join(dir_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(s, folder_path)
        if os.path.isdir(s):
            continue
            # organize_files(s)



def main():
    dir_path = "."
    file_types = count_files_by_extension(dir_path)
    print("Extension\tCount")
    
    for file_extension, count in file_types.items():
        print(f"{file_extension}\t\t{count}")

    organize_files('.')
    

if __name__ == '__main__':
    main()