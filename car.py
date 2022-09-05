print("Start the 'Car' game!\nEnter 'help' command to now about the game!")
command = ""
start = False
while True:
    a = str(input("> ")).upper()
    if a == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif a == 'START':
        if start :
            print("Car is already started...")
        else:
            start = True
            print("Car started...ready to go....")
    elif a == 'STOP':
        if not start:
            print("car is already stopped...")
        else:
            start = False    
            print("Car has stopped...")
    elif a == 'QUIT':
        break
    else:
        print("I dont understand that...")
