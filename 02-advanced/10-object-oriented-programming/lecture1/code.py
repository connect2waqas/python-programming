# class AIstudent:
#     def __init__(self , name, course, age):
#         self.name = name
#         self.age = age
#         self.course = course
#         self.progress = 0
    
#     def introduce(self):
#         print(f"Hi I am {self.name} and I am {self.course} engineer. ")
    
#     def study(self,hours):
#         self.progress += hours * 2
#         if self.progress > 100:
#             self.progress = 100
#         print(f'{self.name} studied for {hours}. Progress : {self.progress}%')
#     def show_progress(self):
#         print(f"📈 {self.name}'s progress in {self.course}: {self.progress}%")


# # Create AI students
# student1 = AIstudent("Waqas", "Computer Vision",23)
# student2 = AIstudent("Areeba", "Natural Language Processing",23)

# # Introduce them
# student1.introduce()
# student2.introduce()

# # Simulate studying
# student1.study(5)
# student2.study(3)

# # Show progress
# student1.show_progress()
# student2.show_progress()

# class Employee:
#     def __init__(self,ag,sal):
#         self.salary = sal
#         self.age = ag
    
#     def display(self):
#         print(f"Salary is {self.salary} and age is {self.age}")


# e1 = Employee(23,2500)
# e2 = Employee(20,5000)

# print(f"The employee age is: {e1.age} ")
# print(f"The employee salary is: {e2.salary}")

# e1.display()

class Managnment:
    def __init__(self,name,Roll_no,course):
        self.name = name
        self.Roll_no = Roll_no
        self.course = course
    
    def display(self):
        print(f"Hi My name is {self.name} with roll no {self.Roll_no} and expert in {self.course}")
    
    def change_data(self):
        self.name = input("Name: ")
        self.Roll_no = int(input("Roll_No: "))
s1 = Managnment("Areeba","F24-0441",["ML","DL","NLP"])
s2 = Managnment("Waqas","F24-0440",["DS","AI","CV"])

# print(f"Roll NO: {getattr(s1,"Roll_no".capitalize())}  Courses: {getattr(s1,"course")}")
# print(f"Roll NO: {getattr(s2,"Roll_no")} Courses: {getattr(s2,"course")}")

# setattr(s2,"Age",20)
# print(f"Sudent {getattr(s2,"Roll_no")} age are: {getattr(s2,"Age")}")

s1.change_data()
print(s1.__dict__)