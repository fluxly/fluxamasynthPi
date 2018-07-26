import fluxamasynthpi
from time import sleep
import random

while (1): 
    note = random.randint(0, 127)
    fluxamasynthpi.noteOn(0, note, 127)
    sleep(float(random.randint(0, 250))/1000)
    fluxamasynthpi.noteOff(0, note)

