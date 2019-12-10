import random
def list():
    num = random.randint(1, 10)
    list = random.sample(range(1, 101), num)
    print("Random number list is : " + str(list))
list()
