# openaitest.py

from config import openai_api_key
import openai

# Set API key
openai.api_key = openai_api_key

# Example API call
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print response
print(response['choices'][0]['message']['content'])
