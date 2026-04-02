from map import map
import time

objects = []

def osu_to_screen(ox, oy):
    x = int(int(ox) * 2.25 + 384)
    y = int(int(oy) * 2.25 + 126)
    return x, y

for obj in map.split("[HitObjects]\n")[1].split("\n"):
    #time.sleep(0.5)
    x, y, delay = obj.split(",")[:3]
    finalx, finaly = osu_to_screen(x, y)
    objects.append((finalx, finaly, delay))
    print(objects)
    #objects.find
    print(obj.split())
    