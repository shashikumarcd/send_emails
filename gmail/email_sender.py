import smtplib
from email.message import EmailMessage
from datetime import datetime

SENDER = "indobuster81@gmail.com"
RECEIVERS = ["info-ind@1xbet-team.com", "accounting@1xbet-team.com", "security-en@1xbet-team.com", "india@1xbet-team.com", "marketing@1xbet-team.com"] #"hitarth.sk@gmail.com"
APP_PASSWORD = "jyrtgsngendmatip" #"dvwucpgmcmisckla"
INTERVAL = "60"  # seconds
SUBJECT = "Final Warning: Pending Payment of INR 40,000"
BODY = "Your continued delay and lack of resolution are unacceptable. " \
"I have fulfilled my obligations in good faith, and the withdrawal payment remains unpaid." \
"consider this is a final warning. If the due amount is not settled immediately, " \
"I will be compelled to proceed with what ever i'm capable of to recover the funds owed to me. "

def send_once():
    msg = EmailMessage()
    
    msg["Subject"] = f"{SUBJECT} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    msg["From"] = SENDER
    msg["To"] = ", ".join(RECEIVERS)
    msg.set_content(f"{BODY}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, APP_PASSWORD)
        server.send_message(msg)

try:
    while True:
        try:
            send_once()
            print(f"Email sent to {', '.join(RECEIVERS)} at {datetime.now().isoformat()}")
        except Exception as e:
            print("Send error:", e)        
except KeyboardInterrupt:
    print("Stopped by user")