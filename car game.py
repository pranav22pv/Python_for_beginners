command = ""

while True:
    command = input("> ").lower()
    if command == "help":
        print('''        start to start the car
        stop to stop the car
        quit to exit        ''')
    elif command == "start":
        print("car started")
    elif command == "stop":
        print("car stoped")
    elif command == "quit":
        break
    else:
        print("sorry i cannot understand that ")