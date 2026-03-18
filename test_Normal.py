import time
import random

p = print

lol = [1, 2, 0, 3245, 74, 3, 4, 9, 5, 6, 7]
lol.sort()
p(lol)

p = print

l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
l2 = ["a", "b", "c", "d", "e"]
rc = random.choice(l2)
print(rc)
print(l)

random.shuffle(l)
print(l)

e = time.localtime()
d = time.get_clock_info("perf_counter")
p(e)
p(d)
