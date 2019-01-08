from numpy.random import *
import json
import ThingSpeak

if __name__=='__main__':
    with open('info.json') as f:
        info = json.load(f)

    r = randint(0, 100, info['Data']['num'])

    ThingSpeak.testfunc(info['ThingSpeak'], info['Data'], r)

