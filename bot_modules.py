import random
import requests
import json
import os
from methods import *
from flask import Flask, render_template, request, make_response

app = Flask(__name__)
timestamp = ''
@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/challenge', methods=['GET','POST'])
def start_challenge():
    params = request.json
    print(params)
    event_type = params['event']['type']
    if (event_type == 'app_mention'):
        return postMessage('게임을 시작하지')
    if (event_type == 'message' and params['event']['text'].find('GO') > 0):
        members = getMemebersFromImogi(timestamp)
        print('후보자들: ' + members)
        return postMessage('후보들: ' + members)
    
    # message = "[%s] 이벤트 핸들러를 찾을 수 없습니다." % event_type
    # return make_response(message, 200, {"X-Slack-No-Retry": 0})

# def get_user():

# @app.route('/app_mention', methods=['POST'])
# def start_game():
#     postMessage('게임을 시작하지')

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5020, threaded=True)


# @app.route('/get', methods=['GET'])
# def start_challenge():
#     print('hello')
#     return render_template('hello')
