import twstock
from linebot.models import (
       QuickReply, QuickReplybutton, TextSendMessage, MessageAction
)


class StcokReplier(object):
    def __init__(self, line_bot_api, token, search_stock_price_text, search_stock_code_text, search_foreign_investment_text):
        self.line_bot_api = line_bot_api
        self.token = token
        self.search_stock_price_text = search_stock_price_text
        self.search_stock_code_text = search_stock_code_text
        self.search_foreign_investment_text = search_foreign_investment_text

    def handle(self, token, user_message):
        if user_message == self.search_stock_price_text:
            self.menu_search_stock_price()
            return
        if user_message == self.search_stock_code_text:
            self.menu_search_stock_code()
            return
        if user_message == self.search_foreign_investment_text:
            self.menu_search_foreign_investment()
            return
        user_entries = user_message.split()
        if len(user_entries) == 2 and user_entries[0] == self.search_stock_price_text:
            if user_entries[1] in twstock.codes:
                self.search_stock_price(user_entries[1])
            return

    def menu_search_stock_price(self):
        stock_list = [(2609, "陽明"), (2330, "台積電")]
        quick_stock_menu = [QuickReplybutton(action=MessageAction(label="{}".format(stock_name),
                                             text="{} {}".format(self.search_stock_price_text, stock_id))) for stock_id, stock_name in stock_list]
        quick_button_menu = TextSendMessage(text="點選下方股票名稱查詢，或者直接輸入「查詢股價 2330」查詢股價", quick_reply=QuickReply(items=quick_stock_menu))
        self.line_bot_api.reply_message(self.token, quick_button_menu)

    def menu_search_stock_code(self):
        pass

    def menu_search_foreign_investment(self):
        pass

    def search_stock_price(self, stock_code):
        stock_info = twstock.realtime.get(stock_code)
        stock_name = stock_info["info"]["name"]
        stock_price = stock_info["realtime"]["latest_trade_price"]
        response_message = "「{}({})」目前的股價為「{}」".format(stock_name, stock_code, stock_price)
        self.line_bot_api.reply_message(self.token, TextSendMessage(text=response_message))

    def search_stock_code(self):
        pass

    def search_foreign_investment(self):
        pass
