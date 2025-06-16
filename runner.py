# Runs all processes here;

# Example usage
from fetch_latest_news import fetch_latest_news_with_content
from llm import generate_with_tinyllama, generate_with_gemini
from prompts_to_llama import build_summarization_prompt


if __name__ == "__main__":
    API_KEY = "f528642ee43960832634d4338db8ec92"
    CATEGORY = ["technology", "business"]
    TOP_K = 10

    news = fetch_latest_news_with_content(CATEGORY, TOP_K, API_KEY)
    user_prompt = build_summarization_prompt(news)
    print(user_prompt)
    exit()
    answer_generated = generate_with_gemini(prompt=user_prompt)
    print(answer_generated)