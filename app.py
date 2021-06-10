#name = input("Instast dir navn? ")
#if len(name) < 3:
#    print("Navn skal have mindst 3 karakterer")
#elif len(name) > 50:
#    print("Navn kan max have 50 karakterer")
#else:
#    print("Navn er ok")

weight = input("Din vægt? ")
x = input("(P)und eller (K)ilo ")
kilo = int(weight) / 2
pund = int(weight) * 2
if x == "P" or x == "p":
    print(f"Vægt i kilo {kilo}")
elif x == "K" or x == "k":
    print(f"Vægt i pund {pund}")
else:
    print("Du har tastet forkert")

#print("Du vejer " + str(kilo) + " omregnet til kilo")
#age = 47
#is_new = False

#has_credit = False
#price = 1000000
#if has_credit:
#    print("Put down 10% = " + str(price * 0.10 ))
#else:
#    print("Put down 20% = " + str(price * 0.20))
