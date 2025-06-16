import requests
import trafilatura
from typing import List
from datetime import datetime

def fetch_latest_news_with_content(categories: List[str], top_k: int, api_key: str):
    """
    Fetches top news articles across multiple categories with full content.
    
    Args:
        categories (List[str]): List of GNews categories (e.g., ["technology", "business"])
        top_k (int): Total number of top articles to return (combined from all categories)
        api_key (str): Your GNews API key

    Returns:
        List[dict]: List of articles with full content
    """
    url = "https://gnews.io/api/v4/top-headlines"
    seen_urls = set()
    all_articles = []

    for category in categories:
        params = {
            "topic": category.lower(),
            "lang": "en",
            "max": top_k,
            "token": api_key
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"[WARNING] Failed to fetch {category}: {response.status_code}")
            continue

        articles = response.json().get("articles", [])
        
        for article in articles:
            article_url = article.get("url")
            if article_url in seen_urls:
                continue  # skip duplicates
            seen_urls.add(article_url)

            downloaded = trafilatura.fetch_url(article_url)
            full_text = trafilatura.extract(downloaded) if downloaded else None

            all_articles.append({
                "title": article.get("title"),
                "url": article_url,
                "publishedAt": article.get("publishedAt"),
                "full_content": full_text or "Could not extract full content.",
                "category": category
            })

    # Optional: sort articles by published date (descending)
    def parse_date(article):
        try:
            return datetime.fromisoformat(article["publishedAt"].replace("Z", "+00:00"))
        except:
            return datetime.min

    sorted_articles = sorted(all_articles, key=parse_date, reverse=True)

    return sorted_articles[:top_k]
