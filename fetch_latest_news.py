# Functions to retrieve and process latest info from news api;

import requests
import trafilatura

def fetch_latest_news_with_content(category: str, top_k: int, api_key: str):
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "topic": category.lower(),
        "lang": "en",
        "max": top_k,
        "token": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code} - {response.text}")
    
    data = response.json()
    articles = data.get("articles", [])

    full_articles = []
    for article in articles[:top_k]:
        article_url = article.get("url")
        downloaded = trafilatura.fetch_url(article_url)
        full_text = trafilatura.extract(downloaded) if downloaded else None

        full_articles.append({
            "title": article.get("title"),
            "url": article_url,
            "publishedAt": article.get("publishedAt"),
            "full_content": full_text or "Could not extract full content."
        })

    return full_articles

# Example usage
if __name__ == "__main__":
    API_KEY = "f528642ee43960832634d4338db8ec92"
    CATEGORY = ["technology", "business"]
    TOP_K = 3

    news = fetch_latest_news_with_content(CATEGORY, TOP_K, API_KEY)
    for idx, article in enumerate(news, 1):
        print(f"\n[{idx}] {article['title']}")
        print(f"Published: {article['publishedAt']}")
        print(f"URL: {article['url']}")
        print(f"\nFull Content:\n{article['full_content']}...")  # print first 1000 chars