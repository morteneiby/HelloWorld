numbers ={
    "1": "en",
    "2": "to",
    "3": "tre",
    "4": "fire",
    "5": "fem",
    "6": "seks",
    "7": "syv",
    "8": "otte",
    "9": "ni"
}
phone = input("Indtast telefonnummer: ")
txt = ""
for x in phone:
    txt = txt + " " + numbers.get(x)
print(txt)

def square(numb):
    result = numb * numb
    return result


print(square(3))

class Person:
    def talk(self):
        print("Jeg taler dansk")

p1 = Person()
p1.talk()