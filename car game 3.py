command = ""
status = 0
while True:
    command = input("> ").lower()
    if command == "help":
        print('''        start to start the car
        stop to stop the car
        quit to exit        ''')
    elif command == "start":
        if status == 1:
            print("car is already started !")
        else:
            print("car started")
            status = 1
    elif command == "stop":
        if status == 0:
            print("car is already stopped !")
        else:
            print("car stopped")
            status = 0
    elif command == "quit":
        break
    else:
          print("sorry I cannot understand that ")

          # instead of status boolean can be used .. and conditions like started = True , command = "start" and if not started {..}

