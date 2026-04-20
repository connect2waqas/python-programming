# Module 12 – OS and System Operations

## What you will learn
- Navigating the filesystem from Python using the `os` module
- Getting and changing the current working directory
- Listing directory contents
- Creating, renaming, and removing files and directories
- Joining paths safely with `os.path.join()`
- Checking if a file or directory exists
- Running system commands with `subprocess`

## Files
| File | Topics covered |
|------|---------------|
| `os.py` | `os.getcwd()`, `os.chdir()` |

## Key concepts

### Current directory
```python
import os

print(os.getcwd())          # print current directory
os.chdir("/some/other/path")  # change directory
print(os.getcwd())          # confirm change
```

### Listing files
```python
import os

entries = os.listdir(".")          # list current directory
for entry in entries:
    print(entry)
```

### Joining paths (safe, cross-platform)
```python
import os

base = "/home/user/projects"
filename = "data.txt"
full_path = os.path.join(base, filename)
print(full_path)   # /home/user/projects/data.txt
```

### Checking existence
```python
import os

if os.path.exists("data.txt"):
    print("File found!")
else:
    print("File not found.")

print(os.path.isfile("data.txt"))   # True if it's a file
print(os.path.isdir("mydir"))       # True if it's a directory
```

### Creating and removing directories
```python
import os

os.makedirs("new/nested/dir", exist_ok=True)   # create (including parents)
os.rmdir("empty_dir")                           # remove empty directory
```

### Renaming and deleting files
```python
import os

os.rename("old_name.txt", "new_name.txt")
os.remove("unwanted.txt")
```

### Running a system command
```python
import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
```

## Practice exercises
1. Write a script that lists all `.py` files in the current directory.
2. Write a script that creates a folder `output/`, writes three `.txt` files into it, then lists them.
3. Write a function `find_files(directory, extension)` that recursively finds all files with a given extension using `os.walk()`.
