# -*- coding: utf-8 -*-
import logging
import twstock
from flask import Blueprint, json, request
from service import HelloService
from linebot import (
        LineBotApi, WebhookHandler
)
from linebot.exceptions import (
        InvalidSignatureError
)
from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage
)

YOUR_CHANNEL_ACCESS_TOKEN = ""
YOUR_CHANNEL_SECRET = ""

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

chatbot_api = Blueprint("chatbot_api", __name__)



@chatbot_api.route("/chatbot", methods=["POST"])
def chatbot_handler():
    # Authetification
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    # Retrieve Data
    req = request.get_json()

    # handler webhook
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    user_message_entries = user_message.split(" ")
    if len(user_message) == 1:
        if user_message == "查詢股價":
            quick_stock_menu = [ QuickReplybutton(action=MessageAction(label="{}".format(stokc_name), text="股價 {}".format(stock_id))) for stock_id, stock_name in stock_list]
            button_menu = TextSendMessage(text="點選下方股票名稱查詢，或者直接輸入「股價 2330」查詢股價", quick_reply=QuickReply(items=quick_stock_menu))
            line_bot_api.reply_message(event.reply_token, button_menu)
        elif user_message == "查詢股票代號":
            pass
        elif user_message == "查詢外資買賣超":
            pass
        else:
            pass
    elif len(user_message) == 2:
        if user_message_entries[0] == "股價":
            response_message = "幫您查詢"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response_message))

    if user_message in twstock.codes:
        stock_info = twstock.realtime.get(user_message)
        stock_name = stock_info["info"]["name"]
        stock_price = stock_info["realtime"]["latest_trade_price"]

        response_message = "幫您查詢{}[{}]目前的股價為{}".format(stock_name, user_message, stock_price)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response_message))
    else:
        error_message = "對不起，我看不懂這個股票代號"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=error_message))

        
