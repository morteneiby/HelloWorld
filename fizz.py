def fezz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FezzBuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fezz"
    else:
        return input


print(fezz_buzz(16))