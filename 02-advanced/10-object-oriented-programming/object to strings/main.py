# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __str__(self):
#         return "Point ({}, {})".format(self.x,self.y)
    
#     def __add__(self,other):
#         return Vector(self.x + other.x,self.y + other.y)
#     def __sub__(self,other):
#         return Vector(self.x - other.x, self.y - other.y)
    
# # Usage
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# print(v1 + v2)
# print(v1 - v2)



# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def midpoint(self, other):
#         mx = (self.x + other.x) / 2
#         my = (self.y + other.y) / 2
#         return Point(mx, my)

# p = Point(2, 4)
# q = Point(6, 8)
# m = p.midpoint(q)
# print(m.x, m.y)  # → 4.0 6.0


# class Rectangle:
#     def __init__(self, x, y, w, h):
#         self.corner = Point(x, y)
#         self.width = w
#         self.height = h

#     def center(self):
#         cx = self.corner.x + self.width / 2
#         cy = self.corner.y + self.height / 2
#         return Point(cx, cy)

# rect = Rectangle(0, 0, 20, 10)
# c = rect.center()
# print(c.x, c.y)  # → 10.0 5.0


# print(Point(3, 4).midpoint(Point(7, 8)).midpoint(Point(5, 0)))


# L = ["Cherry", "Apple", "Blueberry"]

# print(sorted(L))
# print(sorted(L, key=len))
# #alternative form using lambda, if you find that easier to understand
# print(sorted(L, key= lambda x: len(x)))

# class Fruit():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
# for f in sorted(L, key=lambda x: x.price):
#     print(f.name)
    


# class Fruit():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def sort_priorty(self,):
#         return self.price
    

#     def __lt__(self,other_instance):
#         return self.price < other_instance.price


# L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
# print("-----sorted by price, referencing a class method-----")
# for f in sorted(L):
#     print(f.name)

# print("---- one more way to do the same thing-----")
# for f in sorted(L,key=lambda x: x.sort_priorty()):
#     print(f.name)

# class MyClass:
#     class_lst = [1,2]
#     def __init__(self):
#         self.instance_lst = [3,4,5]

# inst_1 = MyClass()
# inst_2 = MyClass()
# print(inst_1.instance_lst is inst_2.instance_lst,inst_1.class_lst is inst_2.class_lst)


# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):

#         self.x = initX
#         self.y = initY

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#     def move(self, dx, dy):
#         self.x = self.x + dx
#         self.y = self.y + dy


# #testing class constructor (__init__ method)
# p = Point(3, 4)
# assert p.y == 4
# assert p.x == 3

# #testing the distance method
# p = Point(3, 4)
# assert p.distanceFromOrigin() == 5.0

# #testing the move method
# p = Point(3, 4)
# p.move(-2, 3)
# assert p.x == 1
# assert p.y == 7


# from random import randrange

# class Pet():
#     boredom_decrement = 4
#     hunger_decrement = 6
#     boredom_threshold = 5
#     hunger_threshold = 10
#     sounds = ["Mrrp"]

#     def __init__(self, name = "Kitty"):
#         self.name = name
#         self.hunger = randrange(self.hunger_threshold)
#         self.boredom = randrange(self.hunger_threshold)
#         self.sounds = self.sounds[:]

#     def clock_tick(self):
#         self.boredom +=1
#         self.hunger +=1
    
#     def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             return "Happpy"
#         elif self.hunger > self.hunger_threshold:
#             return "Hungry"
#         else:
#             return "Bored"
    
#     def __str__(self):
#         state = "I'm " + self.name + "."
#         state += " I feel " + self.mood() + "."
#         return state
#     def teach(self,word):
#         self.sounds = self.sounds.append(word)
#         self.reduce_bordem()
#     def reduce_hunger(self):
#         self.hunger = max(0, self.hunger - self.hunger_decrement)
    
#     def reduce_bordem(self):
#         self.boredom = max(0,self.boredom - self.boredom_decrement)
    
#     def feed(self):
#         self.reduce_hunger()

    

#     def hi(self):
#         print(self.sounds[randrange(len(self.sounds))])
#         self.reduce_bordem()

# p1 = Pet()
# print(p1)

# for i in range(10):
#     p1.clock_tick()
#     print(p1)

# p1.feed()
# p1.hi()
# p1.teach("Hello")

# for i in range(10):
#     p1.hi()
# print(p1)


