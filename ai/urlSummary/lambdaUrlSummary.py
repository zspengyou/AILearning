import os
import json
import requests
import base64
from openai import OpenAI

def lambda_handler(event, context):
    """
    AWS Lambda handler function

    Args:
        event (dict): AWS Lambda Event object
        context (object): AWS Lambda Context object

    Returns:
        dict: Response containing the summary or error message
    """
    print(event)

    if event["requestContext"]["http"]["method"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS, POST, GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": ""
        }
    # Check if the URL is provided in the event
    body = get_json_body(event)
    if 'url' not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'URL not provided in the request'
            })
        }

    url = body['url']

    # Get OpenAI API key from Lambda environment variables
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'OPENAI_API_KEY environment variable not set'
            })
        }

    # Fetch content
    content = fetch_url_content(url)
    if not content:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to fetch URL content'
            })
        }

    # Generate summary
    summary = summarize_text(content)
    if not summary:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to generate summary'
            })
        }

    # Return successful response
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",  # Allow all origins
            "Access-Control-Allow-Methods": "OPTIONS, POST, GET",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        'body': json.dumps({
            'url': url,
            'summary': summary
        })
    }

def fetch_url_content(url):
    """
    Fetch content from a given URL

    Args:
        url (str): The URL to fetch content from

    Returns:
        str: The text content from the URL
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {str(e)}")
        return None

def get_json_body(event):
    if event.get("isBase64Encoded", False):
        # Decode the base64-encoded body
        decoded_body = base64.b64decode(event["body"]).decode("utf-8")
    else:
        decoded_body = event["body"]

    # Parse JSON
    return json.loads(decoded_body)

def summarize_text(text):
    """
    Summarize the given text using OpenAI's API

    Args:
        text (str): Text to summarize

    Returns:
        str: Summarized text
    """
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Please provide a concise summary of the following text"},
                {"role": "user", "content": text}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in summarization: {str(e)}")
        return None