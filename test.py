import smtplib
from email.mime.text import MIMEText

# === CONFIG ===
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "melikovnurlandodo@gmail.com"
EMAIL_PASSWORD = "owvm itbh rtbr wngy"  # App password for Gmail
EMAIL_RECEIVER = "oliverfree09@gmail.com"

# === COMPOSE EMAIL ===
subject = "Test Email from Python"
body = "Hello!\n\nThis is a test email sent from Python using SMTP.\n\nBest,\nPython Script"

# MIME setup
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER

# === SEND EMAIL ===
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("✅ Test email sent successfully.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")







# import trafilatura

# url = "https://www.ibm.com/think/topics/dspy"

# downloaded = trafilatura.fetch_url(url)
# full_text = trafilatura.extract(downloaded) if downloaded else None

# print(full_text)


# import requests

# response = requests.post(
#     "http://localhost:11434/api/generate",
#     json={
#         "model": "tinyllama:latest",  # Change to your installed model name
#         "prompt": "Explain quantum entanglement in simple terms.",
#         "stream": False
#     }
# )

# print(response.json()["response"])
