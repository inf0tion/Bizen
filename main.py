from numpy.random import *
import urllib.request
import json

if __name__=='__main__':
    with open('info.json') as f:
        info = json.load(f)

    print('Update a Channel Feed')
    url = 'https://api.thingspeak.com/update?api_key=' + info['api_key']
    r = randint(0, 100, info['num'])
    for i in range(info['num']):
        url = url + '&field{0}={1}'.format(i+1, r[i])
        
    with urllib.request.urlopen(url) as w:
        res = w.read().decode("utf-8")
        print(res)

    print('Get a Channel Feed')
    jsonurl = 'https://api.thingspeak.com/channels/{0}/feeds.json?results={1}'
    jsonurl = jsonurl.format(info['CH'], info['res'])
    with urllib.request.urlopen(jsonurl) as w:
        res = w.read().decode("utf-8")
        print(res)

    print('json')
    jsondata = json.loads(res)
    print(jsondata)

