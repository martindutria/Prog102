import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, help='Insert value to apply fibonacci sequence')
args = parser.parse_args()


def fibonacci_sequence(number):

    if number < 0:
        print("Number must be 0 or more")

    elif number == 0:
        return 0

    elif number == 1 or number == 2:
        return 1

    else:
        return fibonacci_sequence(number - 1) + fibonacci_sequence(number - 2)


print(fibonacci_sequence(35))
