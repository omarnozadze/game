import random

level = int(input("Level: "))

number = random.randint(1, level)


while True:
    try:
        guess = int(input("Guess: "))
        if  guess == number:
            print("Just right!")
            break
        elif guess > number:
            print ("Too large")
        elif guess < number:
            print("Too small!!")
    except:
        continue
