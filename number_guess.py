import random
num= random.randint(1,100)
while True:
    try:
       guess=int(input("guess a number between 1 to 100:"))
    except ValueError:
           print("Enter avalid number")
           continue
    if guess<num:
             print("too low")
    elif guess>num:
             print("Too high")
             
    else:
            print("you guess the number")
            break