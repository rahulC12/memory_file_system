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
```



In-Memory File System Documentation
Implementation Overview:
The in-memory file system is implemented in Python and provides a basic set of commands to interact with a virtual file system stored in memory. The system supports operations such as creating directories, changing the current directory, listing contents, searching for patterns in files, displaying file contents, creating empty files, moving and copying files, and removing files or directories.

Data Structures Used:
File System Structure (file_system):

The file system structure is represented as a dictionary, where keys are directory paths, and values are either subdirectories (another dictionary) or file contents (string for simplicity).
Current Directory (current_directory):

A string representing the current working directory within the file system.
Design Decisions:
Path Handling:

Paths are manipulated using the os.path.join function to ensure platform-independent path handling.
Directory Navigation:

Directory navigation supports both absolute and relative paths, including navigating to the parent directory using '..' and moving to the root directory using '/'.
User-Friendly Commands:

Commands are designed to mimic typical terminal commands for ease of use. Error messages are provided for invalid inputs or operations.
State Persistence:

The system supports saving and loading the state of the file system. This is useful for persisting the state across different runs of the program.
Dockerfile:
Dockerfile
Copy code
# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run script.py when the container launches
CMD ["python", "./script.py"]
Setup Instructions:
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Build Docker Image:

bash
Copy code
docker build -t in-memory-fs .
Run Docker Container:

bash
Copy code
docker run -it in-memory-fs
Execute File System Commands:

Once inside the Docker container, you can enter file system commands as prompted.
Save and Load State:

To save the state, use the save_state command, e.g., save_state /path/to/state.json.
To load a saved state, use the load_state command, e.g., load_state /path/to/state.json.
Testing:
For testing, you can interact with the file system commands within the Docker container. Ensure that you test various scenarios, including creating and navigating directories, manipulating files, and saving/loading states.

End of Documentation
Please note that this documentation is a basic template, and you should tailor it to fit the specific details and features of your implementation.





