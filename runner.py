# Runs all processes here;

# Example usage
from fetch_latest_news import fetch_latest_news_with_content
from llm import generate_with_tinyllama, generate_with_gemini
from prompts_to_llama import build_summarization_prompt
from email_sender import EmailBuilder
from datetime import datetime
import smtplib
import os 
from dotenv import load_dotenv

from utils import extract_json_values

load_dotenv()

if __name__ == "__main__":
    GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
    CATEGORY = ["technology", "business"]
    TOP_K = 10
    
     # Prepare summary
    news = fetch_latest_news_with_content(CATEGORY, TOP_K, GNEWS_API_KEY)
    user_prompt = build_summarization_prompt(news)
    answer_generated = generate_with_gemini(prompt=user_prompt)

    # Dynamic subject line
    today_str = datetime.now().strftime("%Y-%m-%d")
    subject = f"Ideas for {today_str}"

    # List of recipients
    recipient_list = [
        # "muradaliyev2229@gmail.com",
        "melikovnurlandodo@gmail.com"
    ]

    # Send email to multiple recipients
    email = EmailBuilder(
        subject=subject,
        sender="noreply@yourapp.com",
        recipients=recipient_list
    )

    email.set_text_body(answer_generated)

    # Build and send
    msg = email.build()

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("niconinerstop@gmail.com", os.getenv("GMAIL_APP_CODE"))
        server.send_message(msg)