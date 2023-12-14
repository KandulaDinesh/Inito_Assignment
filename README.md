# In-Memory File System Documentation <br>

## Overview
This In-Memory File System is a Python program that simulates a basic file system in memory. Users can interact with the file system using a command-line interface to perform operations such as creating directories, creating files, moving files, copying files, and more.

## How to Run

1. Make sure you have Python installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/KandulaDinesh/Inito_Assignment.git
   cd your-repository
3. Run the application in the terminal
   ```bash
     python main.py
   
# Commands
#### mkdir <folder_name>: Create a directory.
#### cd <path>: Change the current working directory.
#### ls [path]: List the contents of the specified directory.
#### touch <file_name>: Create an empty file.
#### cat <file_path>: Display the contents of a file.
#### echo <file_path> <content>: Write text to a file.
#### mv <source> <destination>: Move a file or directory.
#### cp <source> <destination>: Copy a file or directory.
#### rm <path>: Remove a file or directory.
#### grep <pattern> [path]: Search for lines containing a pattern in a file.
#### save_state <file_path>: Save the current working directory to a file.
#### load_state <file_path>: Load the current working directory from a file.
#### exit: Exit the file manager.
