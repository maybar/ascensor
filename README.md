# ascensor
Librería gráfica de control de ascensor
Libreria de usos educativo que fascilita de la realización de tests para probar algoritmos de control de ascesonsores.

# Métodos
## elevator(caption)
Es el contructor. 
* caption: Nombre de la ventana gráfica

## destroy()

## execute()
Ejecuta las acciones automáticas del ascensor, como el movimiento del ascensor, la simulación del cierre de puertas, 
o la captura de eventos del teclado.
Esta función debe llamarse periódicamente.

## set_motor(mov)
Establece el estado de movimiento del motor.
* mov : "up", "down", "stop"

## get_motor()
Devuelve el estdo actual del motor: "up", "down", "stop"

## set_door(state):
Comanda el control de las puertas.
* state: "close", "open"

## get_door():
Devuelve el estado actual de las puertas: "close", "open","closing", "opening"
        
## get_floor():
Devuelve el piso actual: 1,2,3,4,5

## set_floor_indicator(floor):
Control del indicador de piso actual
* floor: 1,2,3,4,5

## set_mov_indicator(mov):
Control del indicador de movimiento
* mov: "stop","up","down"

## get_button_call():
Develve el botón de llamada de ascensor: 0,1,2,3,4,5
0: Ningún botón ha sido pulsado.
Los botones de llamanda puede ser controlados por el ratón o usando las teclas: F1,F2,F3,F4,F5

## get_button_int(key):
Develve el botón de piso de la botonera
* key: 0,1,2,3,4,5
0: Ningún botón ha sido pulsado.
Los botones de llamanda puede ser controlados por el ratón o usando las teclas: 1,2,3,4,5

## set_light_call( key, state):
Control el led de llamada de ascensor.
* key: 1,2,3,4,5
* state: "off", "on"

## set_light_int( key, state):
Control el led del selector de piso del ascensor.
* key: 1,2,3,4,5
* state: "off", "on"

# Ejemplo de uso

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

                print (lift.get_button_call())

        def main():
            lift = elevator.elevator("Ascensor1")

            lift.set_motor("stop")
            lift.set_mov_indicator("stop")
            lift.set_door("close")
            lift.set_light_call(1,"on")
            lift.set_light_int(1,"on")
            lift.set_light_int(2,"on")
            lift.set_light_int(3,"on")
            lift.set_light_int(4,"on")
            lift.set_light_int(5,"on")
            try:
                state_machine(lift)    
            finally:
                print("Destroy")
                lift.destroy()
        

        if __name__ == "__main__":

            main()
        
