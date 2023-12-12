import os
import json

class InMemoryFileSystem:
    def __init__(self):
        self.current_directory = '/'
        self.file_system = {}

    def mkdir(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        if new_directory_path not in self.file_system:
            self.file_system[new_directory_path] = {}
        else:
            raise FileExistsError(f"Directory '{directory_name}' already exists.")

    def cd(self, path):
        if path == '/':
            self.current_directory = '/'
        elif path == '..':
            # Move to the parent directory
            self.current_directory = os.path.dirname(self.current_directory)
        elif path.startswith('/'):
            # Move to an absolute path
            self.current_directory = path
        else:
            # Move to a relative path
            self.current_directory = os.path.join(self.current_directory, path)

    def ls(self, path='.'):
        target_path = os.path.join(self.current_directory, path)
        if target_path in self.file_system and isinstance(self.file_system[target_path], dict):
            contents = list(self.file_system[target_path].keys())
            print("\n".join(contents))
        else:
            print(f"No such directory: {path}")

    def grep(self, pattern, file_path):
        target_path = os.path.join(self.current_directory, file_path)
        if target_path in self.file_system and isinstance(self.file_system[target_path], str):
            lines = self.file_system[target_path].split('\n')
            matching_lines = [line for line in lines if pattern in line]
            print("\n".join(matching_lines))
        else:
            print(f"No such file: {file_path}")

    def cat(self, file_path):
        target_path = os.path.join(self.current_directory, file_path)
        if target_path in this.file_system and isinstance(self.file_system[target_path], str):
            print(self.file_system[target_path])
        else:
            print(f"No such file: {file_path}")

    def touch(self, file_path):
        new_file_path = os.path.join(self.current_directory, file_path)
        if new_file_path not in self.file_system:
            self.file_system[new_file_path] = ""
        else:
            raise FileExistsError(f"File '{file_path}' already exists.")

    def echo(self, content, file_path):
        target_path = os.path.join(self.current_directory, file_path)
        if target_path in self.file_system and isinstance(self.file_system[target_path], str):
            self.file_system[target_path] = content
        else:
            print(f"No such file: {file_path}")

    def mv(self, source_path, destination_path):
        source = os.path.join(self.current_directory, source_path)
        destination = os.path.join(self.current_directory, destination_path)
        
        if source in self.file_system:
            self.file_system[destination] = self.file_system.pop(source)
        else:
            raise FileNotFoundError(f"No such file or directory: {source_path}")

    def cp(self, source_path, destination_path):
        source = os.path.join(self.current_directory, source_path)
        destination = os.path.join(self.current_directory, destination_path)
        
        if source in self.file_system:
            self.file_system[destination] = self.file_system[source]
        else:
            raise FileNotFoundError(f"No such file or directory: {source_path}")

    def rm(self, path):
        target_path = os.path.join(self.current_directory, path)
        if target_path in self.file_system:
            del self.file_system[target_path]
        else:
            raise FileNotFoundError(f"No such file or directory: {path}")

    def save_state(self, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump({'current_directory': self.current_directory, 'file_system': self.file_system}, file)
        except Exception as e:
            print(f"Error saving state: {e}")

    def load_state(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.current_directory = data['current_directory']
                self.file_system = data['file_system']
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except Exception as e:
            print(f"Error loading state: {e}")

def process_command(command, file_system):
    parts = command.split(' ')
    operation = parts[0]
    
    if not operation:
        print("Invalid command. Please provide a valid command.")
        return

    try:
        if operation == 'mkdir':
            if len(parts) == 2:
                file_system.mkdir(parts[1])
            else:
                print("Invalid 'mkdir' command. Usage: mkdir <directory_name>")
        elif operation == 'cd':
            if len(parts) == 2:
                file_system.cd(parts[1])
            else:
                print("Invalid 'cd' command. Usage: cd <path>")
        # ... (similar handling for other commands)
        else:
            print(f"Invalid command: {command}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the specified file or directory exists.")
    except FileExistsError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_system = InMemoryFileSystem()
    while True:
        user_input = input('Enter command: ')
        if user_input.lower() == 'exit':
            break
        elif user_input.startswith('save_state'):
            parts = user_input.split(' ')
            file_system.save_state(parts[1])
            print(f"State saved to {parts[1]}")
        elif user_input.startswith('load_state'):
            parts = user_input.split(' ')
            file_system.load_state(parts[1])
            print(f"State loaded from {parts[1]}")
        else:
            process_command(user_input, file_system)

if __name__ == "__main__":
    main()
