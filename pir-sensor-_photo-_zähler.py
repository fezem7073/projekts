from gpiozero import MotionSensor
import time
from picamera2 import Picamera2

pir = MotionSensor(4)
x = 1

while True:
    pir.wait_for_motion()
    print("You moved")
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration())
    picam2.start()
    time.sleep(0.3)
    picam2.capture_file("photo_" + str(x) + ".jpg")
    print("Foto wurde gespeichert als 'photo_" + str(x) + ".jpg'")
    picam2.close()
    time.sleep(2)
    x = x + 1
    pir.wait_for_no_motion()
    print ("ready")