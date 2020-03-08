from flask import jsonify, request, flash, Flask, redirect, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.contrib.fixers import ProxyFix

import pandas as pd
import json
import uuid
import copy
import os
import shutil
import pickle

from ding_di import generate_ding_di
from trade.regression_trade import run_regression

from object.user import User

userInformation = [
    {"name": "admin", "user_id": "admin", "currentAuthority": "admin", "password": "admin"},
    {"name": "user", "user_id": "user", "currentAuthority": "user", "password": "findprocess"},
    {"name": "ebpm", "user_id": "ebpm", "currentAuthority": "user", "password": "ebpm"},
    {"name": "frank", "user_id": "frank", "currentAuthority": "user", "password": "findprocess"},
    {"name": "cong", "user_id": "cong", "currentAuthority": "user", "password": "findprocess"},
    {"name": "long", "user_id": "long", "currentAuthority": "user", "password": "findprocess"},
]
UserList = {}
UserPassword = []
UserNameIdMap = {}
UserTokenIdMap = {}
for i in userInformation:
    UserList[i["user_id"]] = User(i["name"], i["user_id"], i["password"], i["currentAuthority"])
    UserPassword.append((i["name"], i["password"]))
    UserNameIdMap[i["name"]] = i["user_id"]

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = './uploads'
# app.config['WORKSPACE_FOLDER'] = './workspace'
# app.config['UPLOAD_FOLDER'] = '.\\uploads'
# app.config['WORKSPACE_FOLDER'] = '.\\workspace'
app.wsgi_app = ProxyFix(app.wsgi_app)
all_url = "/server/api"


# data = json.load(open("result.json", mode="r"))

# try:
#     shutil.rmtree(app.config['UPLOAD_FOLDER'])
# except FileNotFoundError:
#     pass
# os.mkdir(app.config['UPLOAD_FOLDER'])


def check_user(this_request):
    user_token = this_request.cookies.get('find_process_user_id')
    global UserList, UserTokenIdMap
    if user_token not in UserTokenIdMap:
        return None
    else:
        user = UserList[UserTokenIdMap[user_token]]
    return user


def add_user_on_response(information, user):
    response = jsonify(information)
    response.set_cookie('find_process_user_id', user.token)
    return response


##################################################################################################################
# User management ################################################################################################
##################################################################################################################

@app.route('/')
def hello():
    # global a
    # a = False if a else True
    return jsonify({"a": "Hello from the backend"})


@app.route(all_url + '/currentUser')
def current_user():
    user = check_user(request)
    if user is None:
        return jsonify({"logout": True})
    return jsonify({"name": user.name, "userid": user.user_id, "token": user.token})


@app.route(all_url + '/logout')
def logout():
    user = check_user(request)
    if user is None:
        return jsonify({"logout": True})
    user.clean_token()
    return add_user_on_response({"name": 'user', "userid": "aaa"}, user)


@app.route(all_url + '/login/account', methods=['POST'])
def user_login():
    data = request.get_json()

    user_name = data["userName"]
    password = data["password"]
    type_is = data["type"]  # from antd-pro

    if (user_name, password) in UserPassword:
        user = UserList[UserNameIdMap[user_name]]
        if user.token is not None and user.token in UserTokenIdMap:
            UserTokenIdMap.pop(user.token)
        UserTokenIdMap[user.set_token()] = user.user_id
        return add_user_on_response({"currentAuthority": 'user', "status": 'ok', "type": type_is}, user)
    return jsonify({"currentAuthority": 'guest', "status": 'error', "type": type_is})


@app.route(all_url + '/ding_di')
def ding_di():
    user = check_user(request)
    if user is None:
        return jsonify({"logout": True})

    inter = {"true": True, "false": False}
    code = request.args.get('code')
    combine_switch = request.args.get('combineDingDi')
    adjustment = request.args.get('adjustment')
    data = generate_ding_di(code, inter[combine_switch], inter[adjustment])
    return add_user_on_response(data, user)


@app.route(all_url + '/regress', methods=['POST'])
def regress():
    user = check_user(request)
    if user is None:
        return jsonify({"logout": True})

    data = request.get_json()

    code = data["code"]
    option = data["option"]

    result = run_regression(code, option['invest'], parameter=option, combine_switch=True, strategy=option["strategy"])
    print(result)
    return add_user_on_response(result, user)


if __name__ == '__main__':
    # print(data)
    app.run(host="0.0.0.0")
