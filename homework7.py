import random
def randomsum():
    print("These are the 10 random numbers generated: ")
    count = 0
    add = 0
    while count < 10:
        num = random.randint(1, 101)
        print(num)
        sum = add + num
        count += 1
    print("These is the sum of the 10 random numbers showed above:",add)

randomsum()