import time
import json
import os
import requests
from datetime import datetime
import google.generativeai as genai

# --- জেমিনি এপিআই কনফিগারেশন ---
GOOGLE_API_KEY = "AQ.Ab8RN6II5_Y9sb8oiMSE1wSrOhkslIq3zejqDyOCQPOtsj7ZQQ"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 0.75,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}
model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)

class SuperFastMagicBallAI:
    def __init__(self, telegram_token, chat_id):
        self.telegram_token = telegram_token
        self.chat_id = chat_id
        self.evolution_score = 1.0
        print("=== Magic Ball Neural-Mesh Engine Initialized for 4 Channels ===")

    def send_telegram_alert(self, channel_name, video_title):
        if not self.telegram_token or not self.chat_id:
            return
            
        message = (
            f"🚀 **New 5x Scheduled Script Ready!**\n"
            f"📺 **Channel:** {channel_name}\n"
            f"📝 **Title/Hook:** {video_title}\n"
            f"🕒 **Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message, "parse_mode": "Markdown"}
        try:
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            print(f"[Telegram Error]: {e}")

    def generate_real_ai_script(self, channel_name, category):
        prompt = f"Create a viral, highly engaging YouTube short video title and a short 3-line script hook in Bengali for the channel '{channel_name}' under category '{category}'. Make it unique, catchy, and mysterious."
        try:
            response = model.generate_content(prompt)
            script_content = response.text.strip()
        except Exception as e:
            script_content = f"{category} সম্পর্কিত রহস্যময় ও শিক্ষণীয় ঘটনা - পর্ব {int(self.evolution_score * 10)}"
            print(f"[API Error]: {e}")
            
        self.evolution_score += 0.02 
        return script_content

    def lightweight_storage_save(self, channel_name, data):
        db_file = "lightweight_storage.json"
        db = {}
        if os.path.exists(db_file):
            try:
                with open(db_file, "r", encoding="utf-8") as f:
                    db = json.load(f)
            except:
                db = {}
                
        if channel_name not in db:
            db[channel_name] = []
            
        db[channel_name].append(data)
        
        with open(db_file, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)

    def process_all_channels(self):
        # আপনার স্ক্রিনশট অনুযায়ী সুনির্দিষ্ট ৪টি চ্যানেল
        channels = [
            {"name": "নূর ও ইতিহাস", "category": "Islamic History and Waqiah"},
            {"name": "AuraVoidSpace", "category": "Deep Space and Universe Mysteries"},
            {"name": "DESHI HACKS", "category": "Tech Hacks and Gadgets"},
            {"name": "Md Ebrahim", "category": "Prophets Stories and Quranic Miracles"}
        ]
        
        for ch in channels:
            print(f"\n--- Processing: {ch['name']} ---")
            generated_data = self.generate_real_ai_script(ch['name'], ch['category'])
            
            task_data = {
                "content": generated_data,
                "timestamp": str(datetime.now()),
                "status": "Ready for Colab Render"
            }
            self.lightweight_storage_save(ch['name'], task_data)
            self.send_telegram_alert(ch['name'], generated_data[:50] + "...")
            time.sleep(1)

if __name__ == "__main__":
    TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
    
    engine = SuperFastMagicBallAI(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
    engine.process_all_channels()
