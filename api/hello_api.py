# -*- coding: utf-8 -*-
import logging
from flask import Blueprint, json, request
from service import HelloService

hello_api = Blueprint("hello_api", __name__)


@hello_api.route("/hello", methods=["POST"])
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
    req = request.get_json()

    # Analysis
    user_id = req.get("user_id")

    try:
        # Value Verification
        if not user_id:
            raise ValueError("user_id is not set!")
        # Service
        hello_service = HelloService()
        data = {
            "text": hello_service.hello(user_id)
        }
        return data
    except ValueError:
        logging.error("VALUE ERROR")

