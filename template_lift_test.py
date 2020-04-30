import elevator

def state_machine(lift):
    while True:
        #Here is state machine
        #...
        lift.execute()
        if lift.get_door() == "close":
            lift.set_motor("up")
            lift.set_mov_indicator("up")
        if int(lift.get_floor()) == 1:
            lift.set_motor("stop")
            lift.set_mov_indicator("stop")
            lift.set_floor_indicator(1)
            lift.set_door("open")
                
        print (lift.get_button_int())

def main():
    lift = elevator.elevator("Ascensor1")
    
    lift.set_motor("stop")
    lift.set_mov_indicator("stop")
    lift.set_door("close")
    lift.set_light_call(2,"on")
    lift.set_light_int(5,"on")
    lift.set_light_int(1,"on")
    lift.set_light_int(2,"on")
    lift.set_light_int(3,"on")
    lift.set_light_int(4,"on")
    try:
        state_machine(lift)    
    finally:
        print("Destroy")
        lift.destroy()
        

if __name__ == "__main__":

    main()
        
