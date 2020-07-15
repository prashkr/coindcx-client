import socketio
# import datetime
from pprint import pprint
import json

socketEndpoint = 'wss://stream.coindcx.com'
sio = socketio.Client()

channelName = 'I-BTC_INR'
# channelName = 'coindcx'

sio.connect(socketEndpoint, transports='websocket')
sio.emit('join', {'channelName': channelName})


@sio.on('depth-update')
def on_depth_update(response):
    print("##### Depth #####")
    pprint(json.loads(response['data']))
    print("\n\n")


# @sio.on('new-trade')
# def on_new_trade(response):
#     print("##### New Trade #####")
#     pprint(json.loads(response['data']))
#     print("\n\n")


# t_start = datetime.datetime.now()
# t_end = t_start + datetime.timedelta(seconds=60)

# while t_start <= t_end:
#     t_start = datetime.datetime.now()


# # leave a channel
# sio.emit('leave', {'channelName': channelName})
