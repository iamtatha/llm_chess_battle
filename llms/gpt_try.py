import os
import openai
openai.organization = 
openai.api_key = 

# Use a model from OpenAI (assuming "text-embedding-ada-002" exists for this example)
model_name="gpt-3.5-turbo"

def chat_with_openai(prompt):
    message = {
        'role': 'user',
        'content': prompt
    }

    response = openai.chat.completions.create(
        model=model_name,
        messages=[message]
    )

    # Extract the chatbot's message from the response.
    # Assuming there's at least one response and taking the last one as the chatbot's reply.
    chatbot_response = response.choices[0].message.content
    return chatbot_response



print(chat_with_openai('What is the capital of India?'))