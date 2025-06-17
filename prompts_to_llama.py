def build_summarization_prompt(articles: list) -> str:
    """
    Constructs a prompt to summarize a list of full articles with analytical insights.

    Args:
        articles (list): List of article dicts with 'title', 'full_content', etc.

    Returns:
        str: A single formatted prompt string.
    """
    if not articles:
        return "No articles available for summarization."

    prompt_lines = [(
                "You are a professional news analyst. Your task is to analyze and summarize each news article. \n\n"
                "Each article must be summarized as with the following fields:\n"
                "- title: (string) The title or headline of the article.\n"
                "- key_event: (string) A concise description of the main action, announcement, or result described in the article.\n"
                "- players: (string) Key organizations, companies, products, technologies, or individuals involved.\n"
                "- analysis: (string) A short analytical comment about the implications or significance of the event.\n\n"
                "THen Summarize it in a pretty neat format as one paragraph article, keep it as long as it should be to explain everythin clearly in a precise manner do not use words too much!!!"
                "Give at the end trend of the day and analysis"                
            )]

    prompt_lines.append("Summarize the following news articles from the past day with a clear and concise structure:\n")

    for idx, article in enumerate(articles, 1):
        title = article.get("title", "Untitled")
        date = article.get("publishedAt", "Unknown date")
        url = article.get("url", "")
        content = article.get("full_content", "No content.")

        prompt_lines.append(f"Article {idx}: {title}")
        prompt_lines.append(f"Date: {date}")
        prompt_lines.append(f"Source: {url}")
        prompt_lines.append(f"Content:\n{content}")
        prompt_lines.append("\n" + "-" * 80 + "\n")

    prompt_lines.append(
        "For each article:\n"
        "- Use bullet points to list the **key events or actions** (e.g., 'Company X raised $Y', 'Product Z launched').\n"
        "- Mention any important **players, technologies, sectors, or markets**.\n"
        "- Keep it **brief, factual**, and **clear**.\n"
        "- After each article, add a **short analytical comment or idea** based on the information.\n\n"
        "After reviewing all articles:\n"
        "- Provide a **summary paragraph** describing the general direction, trend, or market sentiment.\n"
    )

    return "\n".join(prompt_lines)
