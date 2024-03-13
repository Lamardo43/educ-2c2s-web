import os
import sys


def list_files(directory):
    files_dict = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = os.path.splitext(filename)[1]
            files_dict.setdefault(file_extension, []).append(filename)

    # Вывод отсортированных файлов
    for ext, files in sorted(files_dict.items()):
        for filename in sorted(files):
            print(filename)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python files_sort.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: The specified path is not a directory.")
        sys.exit(1)

    list_files(directory)
