# -*- coding: utf-8 -*-
import logging
from flask import Blueprint, json, request, current_app
from service import OrderService

order_api = Blueprint("order_api", __name__)


@order_api.route("/order", methods=["POST"])
def order():
    # Retrieve Data
    req = request.get_json()

    # Analysis
    sentence = req.get("sentence")

    # Payload
    payload = {
        "data": {},
        "errorCode": "000",
        "message": "success"
    }

    try:
        # Value Verification
        if not sentence:
            raise ValueError("sentence is empty!")

        # Service
        order_service = OrderService(current_app.config["automaton"])
        nlp_order = order_service.order(sentence)
        payload["data"] = {
            "total": len(nlp_order),
            "order": nlp_order
        }
    except ValueError as err:
        payload["message"] = "{}".format(err)
        payload["errorCode"] = "001"
    except Exception:
        payload["message"] = "{}".format("Unknown Error occurs")
        payload["errorCode"] = "999"
    return payload

