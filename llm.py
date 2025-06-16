# Running llm functions;

import requests
from typing import Optional

def generate_with_tinyllama(prompt: str, model: str = "tinyllama:latest", stream: bool = False, api_url: str = "http://localhost:11434/api/generate") -> Optional[str]:
    """
    Generates a response from the TinyLLaMA model running via Ollama API.

    Args:
        prompt (str): The prompt or question to send to the model.
        model (str): The model name installed in Ollama (default: 'tinyllama:latest').
        stream (bool): Whether to stream the response (default: False).
        api_url (str): URL of the Ollama API endpoint (default: localhost).

    Returns:
        Optional[str]: The generated response string, or None if an error occurred.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json().get("response")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to call TinyLLaMA API: {e}")
    except (KeyError, ValueError) as e:
        print(f"[ERROR] Unexpected response format: {e}")
    
    return None
