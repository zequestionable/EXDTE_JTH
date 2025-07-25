

#Blue LED indicates the game is in standby.
#The user will press a button that will utilise debounce code
#The LED will turn off once they release the button
#After an amount of time the LED will turn back on
#Once the LED comes on the user needs to press the button again as quickly as possible
#It should print their time to the console
#The time delay will be based on the position of a potentiometer (use value / 10000 +1)
#Use PWM to run the LED at half brightness
import board
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP16)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

while True:
    if button1.value is False:
        led.value = True
    if button1.value is False:
        led.value = False
