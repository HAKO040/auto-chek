import pyfiglet
import time
import os
import random
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
import requests

# تنسيق النصوص
Z =  '\033[1;31m' 
X = '\033[2;32m' 
B = '\033[2;36m'
F = '\033[1;33m' 
C = '\033[2;35m'

logo = pyfiglet.figlet_format('shadow')
print(X+logo)

loo = pyfiglet.figlet_format('storm')
print(F+loo)

k = "</>_</>_</>_</>_</>_</>_</>_</>_</>"
print(C+k)

i = "-----------------‐--------------------------------------------------------------------------------------"
print(C+i)

o = "________________________________________________________________"
print(B+o)

# بيانات البوت
token = '6995048446:AAH7cA-k4iQ0rQSTngr8ikYdr19lE8rNkn8'
chat_id = '7168909426'

# بيانات التلجرام
api_id = '15372008'
api_hash = 'ed85c35370cffb1e2cf050e44e635d26'
client = TelegramClient('session', api_id, api_hash)
client.start()

# القناة المراد الإرسال إليها
ch = "@SDBB_Bot"

def generate_random_number():
    length = random.randint(6, 8)
    start_digit = random.choice(['4', '5'])
    number = start_digit + ''.join(random.choices('0123456789', k=length-1))
    return number

while True:
    try:
        cc = generate_random_number()
        client.send_message(ch, f"/bin {cc}")
        time.sleep(random.randint(6, 7))
        mssag = client.get_messages(ch, limit=1)

        # التحقق من الرسالة
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+2)

        print(mssag[0].message)

        # إرسال النتيجة إلى البوت إذا كانت الرسالة تحتوي على "𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅"
        if "𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅" in mssag[0].message:
            msg = mssag[0].message
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}")

        time.sleep(1)
    except Exception as e:
        print(e)
        print(False)
