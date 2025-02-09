import requests
import json

# Lambda function URL
lambda_url = "https://5dgnllzm6imhiiqcpajvwescum0rgotx.lambda-url.us-east-1.on.aws/"

# Request payload
payload = {
    "url": "https://example.com/"
}

# payload = {
#     "body": json.dumps({"url": "https://example.com/"})
# }

headers = {"Content-Type": "application/json"}

# Send POST request
# response = requests.post(lambda_url, json=payload)
response = requests.post(lambda_url, data=json.dumps(payload))
# response = requests.post(lambda_url, json=payload, headers=headers)
# Print response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
