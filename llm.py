# Running llm functions;

import requests
from typing import Optional
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

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


def generate_with_gemini(prompt: str) -> str:
    # Load API key from environment
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # Initialize the model
    model = genai.GenerativeModel("gemini-1.5-flash")  # You can change to "gemini-1.5-pro" if needed

    # Generate response
    response = model.generate_content(prompt)

    # Return response text
    return response.text.strip()

if __name__ == "__main__":
    generate_with_gemini()
