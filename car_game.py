command=""
while command!="quit":
    command=input(">>>>>> ")
    if command=="start":
        print("car started.....")
    elif command=="stop":
        print("car stopped..")
    elif command=="break":
        print("breaks applied....")
    elif command=="help":
        print("""
        start-to start the car
        stop-to stop the car
        break-to apply the break
        quit-to quit the game
        """)
    elif command==quit:
        break
    else:
        print("sorry, I don't understand that!")
        
