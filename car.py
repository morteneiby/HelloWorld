status = 0
while status == 0:
    chooise = input("> ")
    if chooise.upper() == "HELP":
        print("Start - motoren starter ")
        print("Stop - Moteren stoppet")
        print("Quit - stop spil")
        status += 0
    elif chooise.upper() == "START":
        print("Motor er nu startet")
        status += 0
    elif chooise.upper() == "STOP":
        print("Motor er nu stoppet")
        status += 0
    elif chooise.upper() == "QUIT":
        status += 1
    else:
        print("Jeg forstår ikke din kommando")
