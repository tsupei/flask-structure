# -*- coding: utf-8 -*-
import logging
import traceback
from flask import Blueprint, json, request, current_app
from service import OpinionService

opinion_api = Blueprint("opinion_api", __name__)

@opinion_api.route("/opinion", methods=["POST"])
def opinion():
    '''
    Request: {
        "keyword": "",
        "complete": True,
        "limit": 5
    }
    :return:
    Response: {
        "data":{
            "isFound": boolean,
            "keyword": str,
            "opinions":  list,
            "count": int,
        },
        "message": "" // Success, Error Message
        "errorCode": ""
    }
    [
        {
            'concept': '發明專利',
            'descriptions': [],
            'count':  
        }
    ]
    '''

    # Retrieve Data
    req = request.get_json()

    # Get attributes
    keyword = req.get("keyword")
    complete = req.get("complete", True)
    limit = req.get("limit", 0)

    # Payload
    payload = {
        "data": {},
        "errorCode": "",
        "message": ""
    }

    try:
        # Check api requests
        if not keyword:
            raise ValueError("ValueError: keyword is None")
        if type(keyword) != str:
            raise TypeError("TypeError: keyword should be string while {}".format(type(keyword)))
        if type(limit) != int:
            raise TypeError("TypeError: limit should be int while {}".format(type(limit)))
        if limit < 0:
            raise ValueError("ValueError: limit should be integer while {}".format(limit))

        # Service
        opinion_service = OpinionService(current_app.config["database"])
        match = opinion_service.find_candicates(keyword, complete=complete)

        payload["data"] = {
            "opinions": match,
            "count": len(match),
            "isFound": True if match else False,
            "keyword": keyword
        }
        payload["message"] = "Success"
        payload["errorCode"] = "000"

    except ValueError as err:
        payload["message"] = "{}".format(err)
        payload["errorCode"] = "001"
    except TypeError as err:
        payload["message"] = "{}".format(err)
        payload["errorCode"] = "002"
    except Exception :
        logging.error(traceback.format_exc())
        payload["message"] = "Unexpected Error!"
        payload["errorCode"] = "999"
    return payload