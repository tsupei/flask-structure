# -*- coding: utf-8 -*-
import logging
from flask import Blueprint, json, request
from service import HelloService

hello_api = Blueprint("hello_api", __name__)

@hello_api.route("/hello", methods=["GET"])
def hello():
    '''
    Request: {
        "user_id": "xxx"
    }
    :return:
    Response: {
        "text": "hello! <user_id>"
    }
    '''

    # Retrieve Data
    return "HELLO"

