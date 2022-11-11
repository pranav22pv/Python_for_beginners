command = ""
status = 0
while True:
    command = input("> ").lower()
    if command == "help":
        print('''        start to start the car
        stop to stop the car
        quit to exit        ''')
    elif command == "start" and status == 0:
        print("car started")
        status = 1
    elif command == "start" and status == 1:
        print("car is already started")
    elif command == "stop" and status == 1:
        print("car stopped")
        status = 0
    elif command == "stop" and status == 0:
        print(" car is already stopped")
    elif command == "quit":
        break
    else:
        print("sorry i cannot understand that ")

        # this code is written on own. easier method by mosh in car game 3.py . refer