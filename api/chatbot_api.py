# -*- coding: utf-8 -*-
import os
from flask import Blueprint, request, abort
from linebot import (
        LineBotApi, WebhookHandler
)
from linebot.exceptions import (
        InvalidSignatureError
)
from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage
)
from replier import StockReplier

YOUR_CHANNEL_ACCESS_TOKEN = os.environ['YOUR_CHANNEL_ACCESS_TOKEN']
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

chatbot_api = Blueprint("chatbot_api", __name__)


@chatbot_api.route("/chatbot", methods=["POST"])
def chatbot_handler():
    # Authetification
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    # handler webhook
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    replier = StockReplier(
            line_bot_api=line_bot_api,
            token=event.reply_token,
            search_stock_price_text="查詢股價",
            search_stock_code_text="查詢股票代號",
            search_foreign_investment_text="查詢外資買賣超"
    )
    replier.handle(user_message)
