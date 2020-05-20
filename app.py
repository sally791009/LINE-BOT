from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('N4HcfeYTzHqiax78HMjv3yiIqrloijEtyf75Gr8jR5jmwum0CM3Gw7pyKTSJQdAAxvWiS8mfr2IKcTBvIXhTsNKdWE1Hum+yBplCKE2gEJFPboMADvLtDTaCJ0Mg/VqDsfGjmwm300K5RxDdwzHc3AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a0c24ae8921f6c3a306043a8ada1d181')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '哎呀，我看不懂你說的東西'
    r2 = '肥肥幫你 call out 真人客服'
    s1 = '初次見面，我是肥肥，你喜歡吃青椒嗎？'
    s2 = '你最性感囉'
    s3 = '我漂亮嗎？'
    s4 = '和我一起去吃熱炒吧'

    if msg == 'hi':
        s1


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()