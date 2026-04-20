print("Welcome to computer quiz game! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay let's play :) ")
score = 0
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memoray":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

print("You got " + str(score)+ " questions correct")
print("You got " + str((score / 4)*100)+ " %.")