import os
import shutil


def copy_files_to_directories(list_files_directories: list, directory_path: str):
    for file_name in list_files_directories:
        if '.' in file_name and not file_name.startswith('.'):
            shutil.copy(directory_path + file_name, directory_path + file_name.split('.')[-1].title() + "s")


def create_directories(list_files_directories: list, directory_path: str):
    for file_name in list_files_directories:
        if '.' in file_name and not file_name.startswith('.'):
            file_type_directory = file_name.split('.')[-1].title() + "s"
            if file_type_directory not in os.listdir(directory_path):
                try:
                    os.mkdir(directory_path + file_type_directory)
                except FileExistsError:
                    print("Directory already exists")
                    continue


def main(directory_path: str):
    os.chdir(directory_path)
    list_files_directories = os.listdir(directory_path)

    create_directories(list_files_directories=list_files_directories, directory_path=directory_path)
    copy_files_to_directories(list_files_directories=list_files_directories, directory_path=directory_path)
    print("Done")


if __name__ == '__main__':
    path = input('Please enter the path of your directory: ')
    main(directory_path=path)
