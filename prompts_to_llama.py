# Prompts to guide results of llama accordingly;

def build_summarization_prompt(articles: list) -> str:
    """
    Constructs a prompt to summarize a list of full articles.

    Args:
        articles (list): List of article dicts with 'title', 'full_content', etc.

    Returns:
        str: A single formatted prompt string.
    """
    if not articles:
        return "No articles available for summarization."

    prompt_lines = ["Summarize the following news articles clearly and concisely:\n"]

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

    prompt_lines.append("Provide a summary for each article, and then an overall insight if possible.")
    return "\n".join(prompt_lines)
