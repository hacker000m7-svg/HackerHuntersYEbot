import os
import telebot
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import logging

# إعداد السجلات لمراقبة الأداء في Render
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# الإعدادات الأساسية
TOKEN = "8507105445:AAGf3Io2nV0ENgpN2mBR9SZUOP40MTUD_Ww"
CHANNEL_ID = -1003677186780
# المفتاح الموحد (يجب أن يكون 32 حرفاً)
FERNET_KEY = b'uV9_7p_Z2p6j-S_W_H4cK3r_HUnT3r_YE_S3cr3t_K3y='

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)
cipher = Fernet(FERNET_KEY)

@app.route('/')
def health_check():
    return "HackerHuntersYE Server is Active", 200

@app.route('/api/secure_send', methods=['POST'])
def handle_incoming_data():
    try:
        data = request.get_json()
        if not data or 'payload' not in data:
            return jsonify({"status": "fail", "message": "Missing payload"}), 400
        
        encrypted_payload = data['payload']
        # إرسال البيانات مباشرة للقناة (التشفير يتم في التطبيق لضمان الخصوصية القصوى)
        bot.send_message(
            CHANNEL_ID, 
            f"🛡️ **HH-YE SECURE DATA** 🛡️\n\n`{encrypted_payload}`", 
            parse_mode="Markdown"
        )
        
        logger.info("Data sent to channel successfully.")
        return jsonify({"status": "success", "info": "Data stored safely"}), 200

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
