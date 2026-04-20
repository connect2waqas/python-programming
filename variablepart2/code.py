# small_float = 1.5e2
# print(small_float)

# multiline_string = """hello word by
# waqas ahmad"""
# print(multiline_string)

# nothing = None
# # print("Nothing Here:",type(nothing))

# if nothing is None:
#     print("variable has no value")
# else:
#     print("variable has value",nothing)

# list = []
# print("empty list",type(list))

# variable = [10,20,30,40,50]
# print(variable[0:3])

# print(variable[0:])
# print(variable[0])

# var1 = variable[0] = 80
# print(var1 ,type(var1))


# user_data = ["waqas",23,False,40000]
# print(user_data)
# user_data.append(3000)
# print(user_data)
# user_data1 = user_data.append("ilyas")
# print(user_data1)
# user_data.insert(4,"Helloword!")
# print(user_data)


# user_data.pop()
# print(user_data)
# user_data.pop(2)
# print(user_data)

# removing first occurance

# number = [10,20,30,40,50,60,70]

# number.remove(20)
# print(number)

# number[6] = 90
# print(number)

# number = [10,20,30,40,50,60,70]
# number.clear()

# print(number)
# print(number[-1])

# extend_method

# list_1 = [10,20,30]
# list_2 = [40,50,60]

# list_1.extend(list_2)
# print(list_1)

# print(list_1.copy())
# print(list_1.count(20))
# print(list_1.count(30))


# list_1.reverse()

# print(list_1)


# empty = ()
# print(empty)

# single_value = (20,)
# print(single_value)

# multi_value = ("age",23,True)
# print(multi_value)

# tuple1 = (20,30,40,50)
# print(tuple1[0:1]) # return the first element of tuple


# try:
#     tuple1[0] = 90
# except TypeError as e:
#     print("error",e)

# person_tuple = ("waqas",30,"Ai engineer")

# name, age, status = person_tuple

# print(f"name is {name}")
# print(f"age is {age}")
# print(f"status is {status}")

# Dictionary 

# creating dictionary

# empty_dict = {}
# person_dict = {"name" : "ilyas" , "age" : 18}
# another_dict = dict(city="london", country="UK")

# print(empty_dict)
# print(person_dict)
# print(another_dict)

# accessing the dictionary 2 method exist

# print(person_dict["age"])
# print(person_dict.get("name"))

# print(person_dict.keys)
# for key in person_dict:
#     if key == "name":
#         print("found")
#         break
#     else:
#         print("Not found")

# person_dict1 = {
#     "name" : "waqas khan",
#     "age" : 20,
#     "status" : "student",
#     "address" : "Dir lower",
# }

# print(person_dict1.keys())
# print(person_dict1.values())

# print(person_dict1.items())

# person_dict1["occupaction"] = "Ai engineer"

# print(person_dict1)
# remove_value = person_dict1.pop("occupaction")
# print(remove_value)
# print(person_dict1)

# set

# empty_set = set()
# number_set = {1,2,3,4,5,6,7,8,9,10}
# mix_set = {1,1,"waqas",False,(2,3)}

# print("empty set",empty_set)
# print("number set",number_set)
# print("mix set",mix_set)

# number_set.add(11)
# print(number_set)
# number_set.discard(11) # remove 11 if exist and no error if not exist

# print("union of set",number_set.union(mix_set))
# print("intersection",number_set.intersection(mix_set))
# print("difference", number_set.difference(mix_set))
# print("symmetric difference", number_set.symmetric_difference(mix_set))
# print("symmetric difference",mix_set.symmetric_difference(number_set))