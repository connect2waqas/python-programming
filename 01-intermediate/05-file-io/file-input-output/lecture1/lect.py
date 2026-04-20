import json

d = {"name":"waqas","age":20,"ismarried":False,"Insurrance":None}
name = "Ilyas"
age = "18"
# data = ["bashir",22,False,None]
data1 = ("Roman",22,False,None)
var = None

# print(json.dumps(d))

# print(json.dumps(data))

# print(json.dumps(data1))


data = {
    "age" : 23,
    "city" : "Haripur",
    "Name" : "waqas",
    "Number" :7832042,
    "Subject" :
    [
        "Data Structure",
        "Computer Science",
        "Discrete mathemathics"
    ],
    "Ismarried" : False
}

# f = open("data.json",mode="w")
# json_data = json.dump(data,f,indent=4,sort_keys=True)
# print(json_data)
# print(type(json_data))

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

data1 = json.loads(json_data)
print(data1)
print(type(data1))