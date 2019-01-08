import ambient
import requests

def testfunc(info, datainfo, r):
    am = ambient.Ambient(info['CHID'], info['WRITE_KEY'], info['READ_KEY'], info['USER_KEY'])

    print('{0}'.format(r))

    try:
        res = am.send({'d1':r[0].item(), 'd2':r[1].item()})
        print(res)
        d = am.read(n=datainfo['res'])
        print(d)
    except requests.exceptions.RequestException as e:
        print('request failed: ', e)

