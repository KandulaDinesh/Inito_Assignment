# operations.py

import os
import re
import shutil
import json
from utils import display_error


def menu():
    print("\n======= Menu =======")
    print("1. mkdir <folder_name>")
    print("2. cd <path>")
    print("3. ls [path]")
    print("4. touch <file_name>")
    print("5. cat <file_path>")
    print("6. echo <file_path> <content>")
    print("7. mv <source> <destination>")
    print("8. cp <source> <destination>")
    print("9. rm <path>")
    print("10. grep <pattern> [path]")
    print("11. save_state <file_path>")
    print("12. load_state <file_path>")
    print("13. exit")
    choice = input("Enter your command: ")
    return choice


def mkdir(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Directory '{folder_name}' created successfully!")
    except FileExistsError:
        display_error(f"Directory '{folder_name}' already exists!")
    except OSError as e:
        display_error(f"Error creating directory '{folder_name}': {e}")


def cd(path):
    try:
        os.chdir(path)
        print(f"Current directory changed to '{path}'")
    except FileNotFoundError:
        display_error(f"Directory '{path}' does not exist!")
    except PermissionError:
        display_error(f"Permission denied to access '{path}'")


def ls(path="."):
    try:
        contents = os.listdir(path)
        abs_path = os.path.abspath(path)

        if not contents:
            print(f"The directory '{abs_path}' is empty.")
        else:
            print(f"Contents of '{abs_path}':")
            for item in contents:
                print(item)
    except FileNotFoundError:
        display_error(f"Directory '{path}' does not exist!")


def touch(file_name):
    try:
        open(file_name, "a").close()
        print(f"File '{file_name}' created successfully!")
    except OSError as e:
        display_error(f"Error creating file '{file_name}': {e}")


def cat(command):
    file_path = command[1] if len(command) > 1 else None

    while not file_path:
        file_path = input("Enter the file path: ").strip()

    try:
        with open(file_path, "r") as f:
            content = f.read()
        print(content)
    except FileNotFoundError:
        display_error(f"File '{file_path}' does not exist!")
    except IsADirectoryError:
        display_error(f"'{file_path}' is a directory, not a file.")
    except PermissionError:
        display_error(f"Permission denied to read '{file_path}'.")
    except OSError as e:
        display_error(f"Error reading file '{file_path}': {e}")


def echo(file_path, content):
    try:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Text written to file '{file_path}' successfully!")
    except OSError as e:
        display_error(f"Error writing to file '{file_path}': {e}")


def mv(source, destination):
    print(f"Moving '{source}' to '{destination}'")
    try:
        shutil.move(source, destination)
        print(f"'{source}' moved to '{destination}' successfully!")
    except FileNotFoundError:
        display_error(f"Source path '{source}' does not exist!")
    except PermissionError:
        display_error(
            f"Permission denied to move '{source}' to '{destination}'")
    except shutil.Error as e:
        display_error(f"Error moving file/directory: {e}")


def cp(source=None, destination=None):
    if not source:
        source = input("Enter the source path: ").strip()
    if not destination:
        destination = input("Enter the destination path: ").strip()

    try:
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print(f"File '{source}' copied to '{destination}' successfully!")
        elif os.path.isdir(source):
            shutil.copytree(source, destination)
            print(
                f"Directory '{source}' copied to '{destination}' successfully!")
        else:
            display_error(f"Invalid source path '{source}'.")
    except FileNotFoundError:
        display_error(f"Source path '{source}' does not exist!")
    except PermissionError:
        display_error(
            f"Permission denied to copy '{source}' to '{destination}'.")
    except OSError as e:
        display_error(f"Error copying file/directory '{source}': {e}")


def rm(path=None):
    while not path:
        path = input("Enter the path to remove: ").strip()

    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' removed successfully!")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory '{path}' removed successfully!")
        else:
            display_error(f"Invalid path '{path}'.")
    except FileNotFoundError:
        display_error(f"Path '{path}' does not exist!")
    except PermissionError:
        display_error(f"Permission denied to remove '{path}'.")
    except OSError as e:
        display_error(f"Error removing file/directory '{path}': {e}")


def grep(pattern, path="."):
    try:
        with open(path, "r") as f:
            lines_with_pattern = [
                line for line in f if re.search(pattern, line)]

        if not lines_with_pattern:
            print(
                f"No lines matching the pattern '{pattern}' found in '{path}'.")
        else:
            print(f"Lines matching the pattern '{pattern}' in '{path}':")
            for line in lines_with_pattern:
                print(line.strip())

    except FileNotFoundError:
        display_error(f"File '{path}' does not exist!")
    except PermissionError:
        display_error(f"Permission denied to access '{path}'")
    except OSError as e:
        display_error(f"Error searching file '{path}': {e}")


def save_state(file_path):
    state = {"cwd": os.getcwd()}
    try:
        with open(file_path, "w") as f:
            json.dump(state, f)
        print(f"State saved to '{file_path}' successfully!")
    except OSError as e:
        display_error(f"Error saving state to '{file_path}': {e}")


def load_state(file_path):
    try:
        with open(file_path, "r") as f:
            state = json.load(f)
        os.chdir(state["cwd"])
        print(f"State loaded from '{file_path}' successfully!")
    except FileNotFoundError:
        display_error(f"State file '{file_path}' does not exist!")
    except OSError as e:
        display_error(f"Error loading state from '{file_path}': {e}")


def main():
    while True:
        print("\n======= Menu =======")
        print("1. mkdir <folder_name>")
        print("2. cd <path>")
        print("3. ls [path]")
        print("4. touch <file_name>")
        print("5. cat <file_path>")
        print("6. echo <file_path> <content>")
        print("7. mv <source> <destination>")
        print("8. cp <source> <destination>")
        print("9. rm <path>")
        print("10. grep <pattern> [path]")
        print("11. save_state <file_path>")
        print("12. load_state <file_path>")
        print("13. exit")

        choice = input("Enter your command: ").strip()

        if not choice:
            continue

        command = choice.split()
        action = command[0].lower()

        if action == "exit":
            print("Exiting...")
            break
        elif action == "mkdir":
            mkdir(command[1])
        elif action == "cd":
            cd(command[1])
        elif action == "ls":
            ls(command[1] if len(command) > 1 else ".")
        elif action == "touch":
            touch(command[1])
        elif action == "cat":
            if len(command) > 1:
                cat(command)
            else:
                print("Error: 'cat' command requires a file path.")
        elif action == "echo":
            echo(command[1], " ".join(command[2:]))
        elif action == "mv":
            mv(command[1], command[2])
        elif action == "cp":
            cp(command[1] if len(command) > 1 else None,
               command[2] if len(command) > 2 else None)
        elif action == "rm":
            rm(command[1] if len(command) > 1 else None)
        elif action == "grep":
            grep(command[1], command[2] if len(command) > 2 else ".")
        elif action == "save_state":
            save_state(command[1])
        elif action == "load_state":
            load_state(command[1])
        else:
            display_error("Invalid command! Please enter a valid option.")
