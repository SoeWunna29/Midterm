import math


def nrst_two(x):
    if x > 1:
        y = math.log(x, 2)
        # print(y)
        if y > 0:
            answer = round(y)
            print(x, " is nearest to 2 power", answer)
            print(pow(2, answer))
        else:
            print("buzz")
    else:
        if x > 0.5:
            print(x, " is nearest to 2 power")
            print("1")
        else:
            print(x, " is nearest to 2 power")
            print("0.125")


nrst_two(8)
nrst_two(11.5)
nrst_two(14)
nrst_two(2019)
nrst_two(0.1)
nrst_two(0.75)
nrst_two(1.5)
