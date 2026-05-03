from gpiozero import LED, Button
import time

x = 0
led = LED(21)
button = Button(16)
p = print
t = time.sleep
while True:
    if button.active_time == None:
        p("halten")
        t(0.1)

    x += 1
    led.on()
    time.sleep(0.05)
    led.off()
    button.wait_for_press()
    print(f"lol{x}")
    t(1)