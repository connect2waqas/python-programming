# from random import randrange

# # Here's the original Pet class
# class Pet():
#     boredom_decrement = 4
#     hunger_decrement = 6
#     boredom_threshold = 5
#     hunger_threshold = 10
#     sounds = ['Mrrp']
#     def __init__(self, name = "Kitty"):
#         self.name = name
#         self.hunger = randrange(self.hunger_threshold)
#         self.boredom = randrange(self.boredom_threshold)
#         self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

#     def clock_tick(self):
#         self.boredom += 1
#         self.hunger += 1

#     def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             return "happy"
#         elif self.hunger > self.hunger_threshold:
#             return "hungry"
#         else:
#             return "bored"

#     def __str__(self):
#         state = "     I'm " + self.name + ". "
#         state += " I feel " + self.mood() + ". "
#         # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
#         return state

#     def hi(self):
#         print(self.sounds[randrange(len(self.sounds))])
#         self.reduce_boredom()

#     def teach(self, word):
#         self.sounds.append(word)
#         self.reduce_boredom()

#     def feed(self):
#         self.reduce_hunger()

#     def reduce_hunger(self):
#         self.hunger = max(0, self.hunger - self.hunger_decrement)

#     def reduce_boredom(self):
#         self.boredom = max(0, self.boredom - self.boredom_decrement)

# # Here's the new definition of class Cat, a subclass of Pet.
# class Cat(Pet):
#     sounds = ["Meow"]

#     def chasing_rats(self):
#         return "what are you doing, Pinky? Taking over the world?!"
    
    
    

# p1= Pet("Fido")
# print(p1) # we've seen this stuff before!

# p1.feed()
# p1.hi()
# print(p1)

# cat1 = Cat("Fluffy")
# print(cat1) # this uses the same __str__ method as the Pets do

# cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
# cat1.hi()
# print(cat1)

# print(cat1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!

# class Cheshire(Cat):

#     def smile(self):
#         print(":D :D :D")

# new_cat = Cheshire("Pumpkin")

# new_cat.hi()
# new_cat.chasing_rats()
# new_cat.smile()
# p1 = Pet("Teddy")
# p1.hi()
# print(new_cat)

# print(new_cat.name)
# print(new_cat.boredom_decrement)
# print(new_cat.hunger_threshold)
# print(new_cat.mood())


class Book():
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title,self.author)

class PaperBook(Book):
    def __init__(self, title, author,numPages):
        super().__init__(title, author)
        self.numPages = numPages

class EBook(Book):
    def __init__(self, title, author,size):
        super().__init__(title, author)
        self.size = size
    
class Library:
    def __init__(self):
        self.Book = []
    
    def addBook(self,book):
        self.Book.append(book)
    def getNumBook(self):
        return len(self.Book)
        
myPaperbook = PaperBook("Atomic Habit", "James Clear",500)
myEbook = EBook("wealthy Kpk","Mulana Khan zeb","50kb")
addl = Library()
addl.addBook(myPaperbook)
addl.addBook(myEbook)

print(addl.getNumBook())
