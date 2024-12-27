from env import secret
from openai import OpenAI
import os


def call_chatgpt(message):

    client = OpenAI(api_key=secret)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message.content

def get_response(user_input):

    chat_hist = ''

    if not chat_hist:
        chat_hist = user_input

    prompt = [{
        "role": "system",
        "content": user_input + " " + chat_hist,
        }]

    chat_response = call_chatgpt(prompt)
    return chat_response

# if __name__ == '__main__':
#     user_input = "how are you?"
#     print(get_response(user_input))

#TODO: add response to chat history