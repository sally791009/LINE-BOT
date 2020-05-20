from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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

    if msg in ['hi', 'Hi', '哈囉', '你好']:
        r = '初次見面，我是肥肥，你喜歡吃青椒嗎？'
    elif msg == '你長得好可愛':
        r = '謝謝，我也覺得你很可愛喔'
    elif msg == ['你是誰', '你是誰？'] :
        r = '我是肥肥，我可以幫你訂位喔'
    elif '訂位' in msg: #如果訊息裡提到訂位
        r = '你需要訂位，對嗎？'
    elif msg in ['謝謝', '謝謝妳', '謝謝你', '感謝', '謝啦']:
        sticker_message = StickerSendMessage(
        package_id='11537',
        sticker_id='52002736'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()