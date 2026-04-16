from random import randrange

def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        succeeded = False

        for _ in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))

                if ans == (x + y):
                    succeeded = True
                    score += 1
                    break

                print("EEE")
                continue
            except ValueError:
                print("EEE")
                continue

        if not succeeded:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1 or n > 3:
                raise ValueError
            else:
                return n
        except ValueError:
            pass


def generate_integer(l):
    if l == 1:
       return randrange(0, 10)
    elif l == 2:
        return randrange(10, 100)
    elif l == 3:
       return randrange(100, 1000)

if __name__ == "__main__":
    main()
