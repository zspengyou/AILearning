import os

import dotenv
import requests
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
print(find_dotenv())
load_dotenv(find_dotenv())

def fetch_url_content(url):
    """
    Fetch content from a given URL

    Args:
        url (str): The URL to fetch content from

    Returns:
        str: The text content from the URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

def summarize_test(text):
    """

    :param text:
    :return:
    """
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":"Please provide a concise summary of the following text"},
                {"role":"user","content":text}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in summarization {e}")
        return None

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("OPENAI_API_KEY environment variable not set")
        return
    # url = input("Enter url to summarize")
    url = "https://datagubbe.se/endofciv/"

    content = fetch_url_content(url)
    if not content:
        return
    print(f"content\n{content}")
    summary = summarize_test(content)
    print(f"summary\n{summary}")

if __name__=="__main__":
    main()


