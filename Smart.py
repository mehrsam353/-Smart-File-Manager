from pathlib import Path
import shutil


def get_folder():
    path = input(
        "Enter folder path: "
    ).strip()

    folder = Path(path).expanduser()

    if not folder.exists():
        print("Folder does not exist!")
        return None

    if not folder.is_dir():
        print("This is not a folder!")
        return None

    return folder


def show_files(folder):

    files = list(folder.iterdir())

    if not files:
        print("Folder is empty.")
        return

    for item in files:

        if item.is_file():

            size = item.stat().st_size

            print(
                f"{item.name} "
                f"({size} bytes)"
            )

        else:
            print(
                f"[FOLDER] {item.name}"
            )


def search_files(folder):

    query = input(
        "Search filename: "
    ).lower()

    found = False

    for item in folder.iterdir():

        if query in item.name.lower():

            print(item.name)
            found = True

    if not found:
        print("No files found.")


def rename_file(folder):

    old_name = input(
        "Current filename: "
    )

    old_path = folder / old_name

    if not old_path.exists():
        print("File not found!")
        return

    new_name = input(
        "New filename: "
    )

    new_path = folder / new_name

    if new_path.exists():
        print("A file with this name already exists!")
        return

    old_path.rename(new_path)

    print("File renamed!")


def delete_file(folder):

    name = input(
        "Filename to delete: "
    )

    path = folder / name

    if not path.exists():
        print("Not found!")
        return

    confirm = input(
        "Are you sure? (y/n): "
    ).lower()

    if confirm == "y":

        if path.is_file():
            path.unlink()

        elif path.is_dir():
            shutil.rmtree(path)

        print("Deleted!")


def create_folder(folder):

    name = input(
        "New folder name: "
    )

    new_folder = folder / name

    if new_folder.exists():
        print("Already exists!")
        return

    new_folder.mkdir()

    print("Folder created!")


def main():

    folder = get_folder()

    if folder is None:
        return

    while True:

        print("""
===== SMART FILE MANAGER =====

1. Show Files
2. Search
3. Rename
4. Delete
5. Create Folder
6. Exit
""")

        choice = input("> ")

        if choice == "1":
            show_files(folder)

        elif choice == "2":
            search_files(folder)

        elif choice == "3":
            rename_file(folder)

        elif choice == "4":
            delete_file(folder)

        elif choice == "5":
            create_folder(folder)

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
