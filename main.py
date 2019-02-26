from numpy.random import *
import json
import ThingSpeak
import Ambient

if __name__=='__main__':
    with open('info.json') as f:
        info = json.load(f)

    r = randint(0, 100, info['Data']['num']).tolist()

    ThingSpeak.testfunc(info['ThingSpeak'], info['Data'], r)
    Ambient.testfunc(info['Ambient'], info['Data'], r)

