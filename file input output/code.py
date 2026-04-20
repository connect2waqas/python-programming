"""Case 1: what if file is not present: """
f = open("Sample.txt", "w")
f.write("Hello world")
f.close()
"""The following will now give error becuase it has been closed"""
# f.write("waqas") # ValueError: I/O operation on closed file.

"""What if we have to write multiple lines. then"""
f_1 = open("Sample_1.txt", "w")
f_1.write("Hello world!")
f_1.write("\nHow are you?")
f_1.close()
"we can do this also:"
f_2 = open("Sample_2.txt","w")
f_2.write("Hello world!\nhow are you?")
f_2.close()

"""Case 2: What if we are working or writing in exiting file (present from first) like we are woking in sample_2.txt now"""

f_2 = open("Sample_2.txt", "w")
f_2.write("Ilyas khan\nhow are you?\n")
f_2.close()

"""what happen here: All the exiting file is erase with new string or data: (Notice here)"""
"""Now overcome this issue we will use append mode: which append text to the exiting files"""
f_2 = open("Sample_2.txt", "a")
f_2.write("I am fine") 
f_2.close()
"""Now the text append safely okay."""

"""Second approach for adding multiple lines"""
l = ["Hello\n", "I am waqas\n", "how are you?\n", "I am fine\n"]
f_2 = open("Sample_2.txt","w")
f_2.writelines(l) 
f_2.close()
"""The (writelines) take many thing (list, string, tuples) okay."""
s = ("HEllO WAQAS AHMAD\n","How are you?\n","I am fine")

f_2 = open("Sample_2.txt","w")
f_2.writelines(s)
f_2.close()

"""Reading from files"""

f_2 = open("Sample_2.txt","r")
content = f_2.read()
# print(content)
f_2.close()

"Now for reading just content as just you want"
f_2 = open("Sample_2.txt","r")
content = f_2.read(10)
# print(content)
f_2.close()

f_2 = open("Sample_2.txt", "r")
line_1  = f_2.readline()
line_2 = f_2.readline()
# print(line_1,end="")
# print(line_2,end="")
# f_2.close()
# f_2 = open("Sample_2.txt","r")
# while True:
#     data = f_2.readline()
#     if data == "":
#         break
#     else:
#         print(data,end=" ")
# f_2.close()

"work on with (with)--> context manager"
"""With context is woking on context manager which is object which automatically close the file is cleanup. it is a best way."""

with open("Sample_2.txt","w") as file:
    file.write("Hello how are you now.")
"""with this the file is automatically open and close even by not closing it."""

# with open("Sample_2.txt","r") as file:
#     print(file.read())

# with open("Sample_2.txt", "r") as file:
#     print(file.read(10)) # it will read first 10 character and 
#     print(file.read(10)) # it wil start from next 10 character due to buffer memory and it a benfit for us when loading a large dataset.

# big_L = ["Hello world " for i in range(1000)]

# with open("Big_file.txt", 'w') as f:
#     f.writelines(big_L)


# with open("Big_file.txt", "r") as file:
#     chunk = 100
#     while len(file.read(chunk)) > 0:
#         print(file.read(chunk), end="")
#         file.read(chunk)

# with open("Sample_2.txt","r") as file:
#     print(file.seek(2))
#     print(file.read(10))
#     print(file.tell())

# with open("Sample_2.txt", "w") as file:
#     file.write("Hello")
#     file.seek(0)
#     file.write("X")

# with open("image.png","rb") as image:
#     with open("copy_image.png","wb") as new_image:
#         new_image.write(image.read())
    
# """Serieralization: the process of converting datatypes in json format """
# """Deserielization: the process of converting back the json back to any other datatype"""
# import json
# l = [1,2,3,4,5]
# with open("sample.json","w") as file:
#     json.dump(l,file)

# my_info = {"name" : "Waqas khan",
#            "age" : 21,
#            "Field": "Artificial intelligence"}

# with open("my_info.json","w") as info:
#     json.dump(my_info,info,indent=4)

# with open("my_info.json", "r") as reading:
#     data = json.load(reading)
#     data["name"] , data["age"], data["Field"] = "ilyas", 18, "Electronic Engineering"
#     with open("update.json", "w") as update_data:
#         json.dump(data,update_data, indent=4)

# t = (1,2,3,4,5,6,7,8,9,10)
# with open("number.json","w") as numbers:
#     json.dump(t,numbers)
# with open("number.json","r") as number:
#     numbers = json.load(number)
#     print(numbers)
#     print(type(numbers))
# """So json does not know about the tuple data and therefore it convert the tuple list mean array."""

# """Working on nested dictionary"""

# data = {"name":"Waqas Ahmad",
#         "age": 21,
#         "Marks": [85,95,96,94,93],
#         "Subjects": ["Math","OOP","AI","DataBase","Software Engineering"]}

# with open("Student_Data.json", "w") as student_data:
#     json.dump(data,student_data,indent=4)

# with open("Student_Data.json","r") as student_data:
#     info = json.load(student_data)
#     print(info, type(info))
import json
data = [ {"name":"Ilyas",
        "age": 19,
        "Marks": [85,95,95,93,90],
        "Subjects": ["Math","OOP","AI","DataBase","Software Engineering"]},
         {"name":"Bashir Ahmad",
        "age": 21,
        "Marks": [85,95,86,95,93],
        "Subjects": ["Math","OOP","AI","DataBase","Software Engineering"]},
         {"name":"Abbas Ahmad",
        "age": 12,
        "Marks": [85,93,96,92,94],
        "Subjects": ["Math","OOP","AI","DataBase","Software Engineering"]}
        ]

with open("Student_data.json","w") as file:
    json.dump(data, file,indent=4)

with open("Student_data.json","r") as file:
    data = json.load(file)
    print(data)
    print(type(data))
