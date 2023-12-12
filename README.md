# memory_file_system
This project implements a simple in-memory file system with basic functionalities. The file system supports commands similar to those used in a typical terminal, including directory creation, navigation, file manipulation, and state saving/loading.
# In-Memory File System

## Overview

This project implements a basic in-memory file system with support for common file operations. The file system operates in a simulated environment, and commands can be executed through a command-line interface.

## Features

- `mkdir`: Create a new directory.
- `cd`: Change the current directory.
- `ls`: List the contents of the current or specified directory.
- `grep`: Search for a specified pattern in a file.
- `cat`: Display the contents of a file.
- `touch`: Create a new empty file.
- `echo`: Write text to a file.
- `mv`: Move a file or directory to another location.
- `cp`: Copy a file or directory to another location.
- `rm`: Remove a file or directory.
- Save and load the state of the file system.

## Implementation Details

### InMemoryFileSystem Class

The core functionality is encapsulated in the `InMemoryFileSystem` class. This class maintains the current directory and file system structure in memory.

#### Methods:

- `mkdir`: Creates a new directory.
- `cd`: Changes the current directory.
- `ls`: Lists the contents of a directory.
- `grep`: Searches for a pattern in a file.
- `cat`: Displays the contents of a file.
- `touch`: Creates a new empty file.
- `echo`: Writes text to a file.
- `mv`: Moves a file or directory.
- `cp`: Copies a file or directory.
- `rm`: Removes a file or directory.
- `save_state`: Saves the current state to a file.
- `load_state`: Loads the state from a file.

### Command Processing

The `process_command` function parses user input and calls the appropriate method of the `InMemoryFileSystem` class.

### Main Loop

The `main` function runs an infinite loop, accepting user commands until the user decides to exit. Additionally, it checks for commands to save or load the state.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/in-memory-file-system.git
    ```

2. **Change directory:**

    ```bash
    cd in-memory-file-system
    ```

3. **Run the program:**

    ```bash
    python main.py
    ```

4. **Enter commands in the interactive console.**

### Save and Load State

To save the state:

```bash
save_state /path/to/save/state.json
```
**To load the state:**

```bash
load_state /path/to/load/state.json

```
###
**Docker**
To run the program using Docker:

**Build the Docker image:**

```bash
docker build -t in-memory-file-system .
```
**Run the Docker container:**

```bash


docker run -it in-memory-file-system
```




