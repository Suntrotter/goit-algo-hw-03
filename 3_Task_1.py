import os
import shutil
import argparse

src_dir = r"C:\1\Green card"
dest_dir = r"C:\1\111"

def copy_files(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                src_file_path = os.path.join(root, file)
                extension = os.path.splitext(file)[1].lower()
                dest_subdir = os.path.join(dest_dir, extension[1:])                
                os.makedirs(dest_subdir, exist_ok=True)                
                shutil.copy(src_file_path, dest_subdir)


        print("Files copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them by extension.")
    parser.add_argument("destination_dir", type=str, nargs="?", default="dist", help="Path to the destination directory.")
    args = parser.parse_args()

    

    if not os.path.isdir(src_dir):
        print("Source directory does not exist.")
        return

    try:
        copy_files(src_dir, args.destination_dir)
    except KeyboardInterrupt:
        print("\nProcess interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
