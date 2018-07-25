import fluxamasynthPi
from time import sleep

while (1): 
    noteOn(0, 64, 127)
    sleep(1)
    noteOff(0, 64)
    noteOn(0, 65, 127)
    sleep(1)

