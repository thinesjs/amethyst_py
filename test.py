import json
import random

from openai import OpenAI

from config import Config

config = Config('config.ini')
config.readConfig()

question = "What factors influence your decision to shop at a particular brick-and-mortar store?"

response = OpenAI(api_key=config.getRandApiKey()).chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    temperature=random.random(),
    top_p=0.9,
    seed=random.randint(100, 300),
    messages=[
        {"role": "system",
         "content": "You are answering a questionnaire that aims to understand your shopping habits, preferences, and attitudes towards technology-driven enhancements to the in-store shopping experience. Your answers should output into a JSON with key-pair values. You can use numbers for the keys."},
        {"role": "user", "content": f"{question}"}
    ]
)
json_response = json.loads(response.choices[0].message.content)
keys = list(json_response.keys())
random_key = random.choice(keys)

print(random_key)
# first_key = next(iter(json_response.keys()))

answer = json_response[random_key]

print(answer)
