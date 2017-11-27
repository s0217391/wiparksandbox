from time import sleep
from simple_pin import Pin


reset_pin = Pin(19)
bootmode_pin = Pin(26)

reset_pin.set_pin_direction(Pin.OUTPUT_MODE)
bootmode_pin.set_pin_direction(Pin.INPUT_MODE)

bootmode_pin.set_pin_value(Pin.ENABLE)
sleep(1)
reset_pin.set_pin_value(Pin.ENABLE)
sleep(0.5)
reset_pin.set_pin_value(Pin.DISABLE)

print("Flashed !")
