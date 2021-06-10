a = 10
x = 0


def increment(a):
    print("print3: " + str(a))
    #global a
    a = a + 1
    print("print4: " + str(a))
    return a


def main():
    #a = 10
    global a
    a = a +1
    print("print1: " + str(a))
    increment(a)
    print("print2: " + str(a))


main()

