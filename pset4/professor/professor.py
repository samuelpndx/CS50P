import random


def main():
    level = get_level()

    tries = 0
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y

        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if answer == guess:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {answer}")
                    tries = 0
                    break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    minimum = 10 ** (level - 1) - (10 ** (level - 1)) % 10
    maximum = (10**level) - 1
    return random.randint(int(minimum), maximum)


if __name__ == "__main__":
    main()
