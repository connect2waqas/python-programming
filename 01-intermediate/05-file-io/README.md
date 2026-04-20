# Module 05 – File I/O

## What you will learn
- Opening and closing files in different modes (`r`, `w`, `a`, `rb`, `wb`)
- Reading: `read()`, `readline()`, `readlines()`
- Writing: `write()`, `writelines()`
- The `with` statement (context manager) for safe file handling
- Seeking and telling the file position: `seek()`, `tell()`
- Serialization with `json.dump()` / `json.load()`
- Copying binary files (images)

## Files
| File | Topics covered |
|------|---------------|
| `file-input-output/code.py` | Write/read modes, append mode, writelines, context manager, chunked reading, seek/tell, JSON serialization with nested dictionaries and lists |
| `file-input-output/lecture1/lect.py` | Additional file I/O examples |

## Key concepts

### Opening a file (always prefer `with`)
```python
# Write
with open("sample.txt", "w") as f:
    f.write("Hello, World!\n")

# Read
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
```

### File modes
| Mode | Meaning |
|------|---------|
| `"r"` | Read (file must exist) |
| `"w"` | Write (creates or overwrites) |
| `"a"` | Append (adds to end) |
| `"rb"` / `"wb"` | Binary read / write |

### Reading line by line
```python
with open("sample.txt", "r") as f:
    for line in f:
        print(line, end="")
```

### Writing multiple lines at once
```python
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("sample.txt", "w") as f:
    f.writelines(lines)
```

### JSON serialization
```python
import json

data = {"name": "Waqas", "age": 21, "marks": [85, 90, 95]}

# Save to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Load from file
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])
```

## Practice exercises
1. Write a program that saves your name and age to a `.txt` file and then reads it back.
2. Keep a log file that appends a new entry (with a timestamp) each time the script runs.
3. Store a list of 3 students (each a dictionary with name, age, marks) as JSON, then read it back and print the student with the highest average mark.
