import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
    except ValueError:
        pass
    else:
        break

guess = 0
answer = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 100 or guess < 0:
            raise ValueError
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just Right!")
            break
    except ValueError:
        pass
