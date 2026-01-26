# Lottery Game:

from random import choice


def main():
    winner_logic()


def lottery_num():

    return choice(
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
        ]
    )


def user_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer")


def winner_logic():
    user_input = user_num("Enter num b/w 1 to 10: ")
    #  needed input

    if user_input > 10 or user_input < 1:
        print("Enter number b/w 1 to 10")
        return

    #  winner logic
    if user_input == lottery_num():
        print("Hurray, you have won the lottery")
    else:
        print("You want to try again?")


if __name__ == "__main__":
    main()
