import logging
from unicodedata import normalize as norm
from phue import Bridge
from subprocess import run, PIPE
logging.basicConfig()
b = Bridge('192.168.1.15')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()
lights = b.get_light_objects('name')
logging.info("Detected {} lights:".format(len(lights)))
for l in lights: logging.info("\t{}".format(l))

room = run("whereami predict", shell=True, stdout=PIPE)
room = room.stdout.decode('UTF-8').strip().split('\n')[-1]
room_lights = [l for l in lights if norm("NFKD",room.casefold()) in norm("NFKD",l.casefold())]
print("Detected room {}.\nTurn on {} ? (Y/n)".format(room, room_lights))
if not input().lower() == 'n':
    print("Turning lights on")
    for l in room_lights:
        lights[l].on = True
print("Turn off all other lights ? (Y/n)")
if not input().lower() == 'n':
    print("Turning lights off")
    for n, l in lights.items():
        if not n in room_lights:
            l.on = False
