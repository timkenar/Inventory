from openai import OpenAI

def call_deepseek_api(prompt):
    # Initialize the OpenAI client with DeepSeek's base URL
    client = OpenAI(
        api_key="sk-5aa3ab148fec4917b29a00dda3e1d50f",  # Replace with your DeepSeek API key
        base_url="https://api.deepseek.com",  # DeepSeek API base URL
    )

    # Make the API call
    response = client.chat.completions.create(
        model="deepseek-chat",  # Use "deepseek-chat" for DeepSeek-V3
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        stream=False,  # Set to True for streaming responses
    )

    # Return the generated content
    return response.choices[0].message.content

# import requests
# from openai import OpenAI

# def call_deepseek_api(prompt):
#     api_key="sk-5aa3ab148fec4917b29a00dda3e1d50f"
#     api_url = "https://api.deepseek.com/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer YOUR_DEEPSEEK_API_KEY",
#         "Content-Type": "application/json",
#     }
#     data = {
#         "model": "deepseek-chat",
#         "messages": [{"role": "user", "content": prompt}],
#     }
#     response = requests.post(api_url, json=data, headers=headers)
#     return response.json()