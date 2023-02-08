# File Organizer

A script that counts and organizes files in a directory based on their file extension.

## Requirements

- os
- shutil
- logging

## Usage

The script will run in the current working directory. To run the script, call the `main` function.

## Features

- Counts the number of files in a directory and its subdirectories by file extension.
- Organizes files in the current working directory with `.py`, `.ipynb`, or `.ipynb_checkpoints` extensions into separate folders with the same name as the file.
- Logs all actions in the "logs/file_organizer.log" file.

## Note

The `organize_files` function is currently commented out for subdirectories. Uncommenting this line will allow the script to organize files in subdirectories as well.
