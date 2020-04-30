import elevator

def state_machine(lift):
    sm = "stop"
    dest_floor = 1
    lift.set_floor_indicator(1)
    while True:
        lift_floor = lift.get_floor()
        call_button = lift.get_button_call()
        
            
        if sm == "stop":
            

            if call_button != 0:
                dest_floor = call_button
                lift.set_light_call(dest_floor,"on")
                
                print(dest_floor,lift_floor)
                if dest_floor > lift_floor:
                    lift.set_door("close")
                    dire = "up"
                    sm = "moviendo"
                    lift.set_mov_indicator("up")
                elif dest_floor < lift_floor:
                    lift.set_door("close")
                    dire = "down"
                    sm = "moviendo"
                    lift.set_mov_indicator("down")
            
        elif sm == "moviendo":
            if lift.get_door() == "close":
                lift.set_motor(dire)

            if dest_floor == lift_floor:
                lift.set_motor("stop")
                sm = "stop"
                lift.set_door("open")
                lift.set_light_call(dest_floor,"off")
                lift.set_floor_indicator(int(lift_floor))
                lift.set_mov_indicator("stop")
        lift.execute()


def main():
    lift = elevator.elevator("Ascensor")
    try:
        state_machine(lift)
    finally:
        print("Destroy")
        lift.destroy()
        
        
if __name__ == "__main__":
    main()
            
