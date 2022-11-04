print("Welcome to my Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct Answer')
    score += 1
else:
    print('Incorrect Answer')

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct Answer')
    score += 1
else:
    print('Incorrect Answer')

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct Answer')
    score += 1
else:
    print('Incorrect Answer')

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print('Correct Answer')
    score += 1
else:
    print('Incorrect Answer')

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print('Correct Answer')
    score += 1
else:
    print('Incorrect Answer')

print("Congratulations you got " + str(score) + " questions correct.")
print("Congratulations you got " + str((score / 5) * 100) + "%.")