import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    #print(volume)

    for x in range (0,11):
        if volume > 25000 + (x*2000):
           leds[x].value = 1
        else:
            break
    
    for x in reversed(range(0,11)):
        pvol = volume
        volume = microphone.value
        if pvol<volume:
            break
        if leds[x].value == 1: 
            if volume < (25000 + (x*2000)):
                print(volume)
                sleep(.05)
                leds[x].value = 0



    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
