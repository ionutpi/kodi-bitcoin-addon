import time
import xbmc
import xbmcgui
import random
import requests
import json

if __name__ == '__main__':
    win = xbmcgui.Window(10000)
    h=win.getHeight()
    w=win.getWidth()
    ctrl=xbmcgui.ControlLabel(w/2,int(.05*h), 125, 75, '0', 'font16')
    win.addControl(ctrl)
    win.setFocus(ctrl)

    while True:
        r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data=json.loads(r.text)
        price=data['bpi']['USD']['rate']
        ctrl.setLabel(price)
        time.sleep(60)
