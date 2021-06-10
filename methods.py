import random
import requests
import json
import os
from slack_sdk import WebClient
from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode import SocketModeClient

bot_token = "xoxb-151309704839-2149298764998-iwmeEbLgyAnTQ8y5B5gW0tQN"
user_token = "xoxp-151309704839-1632720355493-2168789046401-baae4b0e13fe432d633b7bf589cfd590"
test_channel = "C020RJVTF09"

client = WebClient(token=bot_token)
user_client = WebClient(token=user_token)

def postMessage(text):
    print('post Message: ', text)
    response = client.chat_postMessage(
        channel=test_channel,
        text=text,
    )

    print('RESPONSE: ' + response)
    return response['message']['ts']

def getMemebersFromImogi(timestamp):
    response = client.reactions_get(
        channel=test_channel,
        ts=timestamp,
    )
    members=[]
    reactions=response['file']['reactions']
    for reaction in reactions:
        members.append(reaction['users'])
    return members

def searchMessage(ts):
    response = client.reactions_get(
        channel=test_channel,
        timestamp=ts
    )

    
