import os
import sys


def search_file(filename):
    for root, dirs, files in os.walk('./'):
        if filename in files:
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as file:
                for _ in range(5):
                    print(file.readline().strip())
            return
    print(f"File {filename} not founded")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_search.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    current_directory = os.path.dirname(os.path.abspath(__file__))

    search_file(filename)
