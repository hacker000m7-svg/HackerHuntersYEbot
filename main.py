from flask import Flask, request, jsonify
import telebot
from cryptography.fernet import Fernet

app = Flask(__name__)

# إعداداتك الخاصة
TOKEN = "8507105445:AAGf3Io2nV0ENgpN2mBR9SZUOP40MTUD_Ww"
CHANNEL_ID = -1003677186780
# مفتاح تشفير ثابت (يجب أن يكون 32 حرفاً)
KEY = b'HackerHuntersYE_SecretKey_32Char!' 
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    return "Server is Live!"

@app.route('/api/data', methods=['POST'])
def handle_data():
    try:
        incoming_data = request.json.get('payload')
        # البوت يرسل البيانات المشفرة للقناة مباشرة
        bot.send_message(CHANNEL_ID, f"🆕 New Encrypted Entry:\n{incoming_data}")
        return jsonify({"status": "done"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
