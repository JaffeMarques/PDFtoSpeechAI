from pathlib import Path
from text_recognition import process_input_folder, process_file

def main():
    files = process_input_folder()
    for file in files:
        process_file(file)

if __name__ == "__main__":
    main()