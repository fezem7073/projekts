from gpiozero import LED, Button
import time

x = 0
led = LED(21)
button = Button(16)

while True:
    x += 1
    led.on()
    time.sleep(0.05)
    led.off()
    button.wait_for_press()
    print(f"lol" + str(x))