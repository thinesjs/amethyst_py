import json
from openai import OpenAI
from config import Config

config = Config('config.ini')
config.readConfig()


def getchatgptanswer(question):
    response = OpenAI(api_key=config.getRandApiKey()).chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system",
             "content": "Imagine you are a human and someone is questioning you to understand your shopping habits, preferences, and attitudes towards technology-driven enhancements to the in-store shopping experience. Your answers should be in speech form (in a sentence, not point form) and output into a JSON."},
            {"role": "user", "content": f"{question}"}
        ]
    )
    json_response = json.loads(response.choices[0].message.content)
    print(f"{question}:{json_response['response']}")
    return json_response['response']
