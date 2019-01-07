from numpy.random import *
import urllib.request
import json

def ThingSpeakTest(info, datainfo, r):
    print('Update a Channel Feed(POST)')
    url = 'https://api.thingspeak.com/update'
    data = 'api_key=' + info['api_key']
    for i in range(datainfo['num']):
        data += '&field{0}={1}'.format(i+1, r[i])
        
    with urllib.request.urlopen(url, data=data.encode('utf-8')) as w:
        res = w.read().decode("utf-8")
        print(res)

    print('Get a Channel Feed')
    jsonurl = 'https://api.thingspeak.com/channels/{0}/feeds.json?results={1}'
    jsonurl = jsonurl.format(info['CH'], datainfo['res'])
    with urllib.request.urlopen(jsonurl) as w:
        res = w.read().decode("utf-8")
        print(res)

    print('json')
    jsondata = json.loads(res)
    print(jsondata)


if __name__=='__main__':
    with open('info.json') as f:
        info = json.load(f)

    r = randint(0, 100, info['Data']['num'])

    ThingSpeakTest(info['ThingSpeak'], info['Data'], r)

