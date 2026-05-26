api/index.py

```python
   from flask import Flask, request
   import telebot

   TOKEN = "8251170342:AAEmuiCsIvfSGk2r3q1h5fwYF7mHjaxjTiY"
   bot = telebot.TeleBot(TOKEN)
   app = Flask(__name__)

   @app.route('/', methods=['POST'])
   def webhook():
       if request.headers.get('content-type') == 'application/json':
           json_string = request.get_data().decode('utf-8')
           update = telebot.types.Update.de_json(json_string)
           bot.process_new_updates([update])
           return ''
       else:
           return 'Invalid request', 400

   @bot.message_handler(func=lambda message: True)
   def echo_all(message):
       bot.reply_to(message, f"【24小時雲端回覆】你說了：{message.text}")
