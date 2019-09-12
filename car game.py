command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('Car already started!')
        else:
            print('Car started...')
            started = True

    elif command == 'stop':
        if not started:
            print("Car already stopped!")
        else:
            print('Car stopped...')
            started = False

    elif command == 'quit':
        break
    elif command == 'help':
        print("""
start   -   car will start
stop    -   car will stop
quit    -   game will quit
        """)
    else:
        print("I don't understand that")
