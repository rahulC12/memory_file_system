# memory_file_system
This project implements a simple in-memory file system with basic functionalities. The file system supports commands similar to those used in a typical terminal, including directory creation, navigation, file manipulation, and state saving/loading.
## Features

- **mkdir:** Create a new directory.
- **cd:** Change the current directory.
- **ls:** List the contents of the current or specified directory.
- **grep:** Search for a specified pattern in a file (bonus feature).
- **cat:** Display the contents of a file.
- **touch:** Create a new empty file.
- **echo:** Write text to a file.
- **mv:** Move a file or directory to another location.
- **cp:** Copy a file or directory to another location.
- **rm:** Remove a file or directory.
- **save_state/load_state:** Save and load the file system state (bonus feature).

## How to Run

1. Ensure you have Python installed.
2. Save the provided script (`in_memory_file_system.py`) to your local machine.
3. Open a terminal or command prompt in the script's directory.
4. Run the script: `python in_memory_file_system.py`.
5. Enter commands as prompted.

## Example Commands

Here's a sequence of example commands to test the file system:

```plaintext
mkdir documents
cd documents
ls
touch file.txt
echo 'Hello, World!' > file.txt
cat file.txt
grep 'Hello' file.txt
mv file.txt /backup/
cp /backup/file.txt /documents/backups/
rm file.txt
ls
save_state state.json
cd /
mkdir photos
ls
exit
