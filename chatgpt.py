import ast
import json
import random
import openai
from openai import OpenAI
from config import Config
from time import sleep

config = Config('config.ini')
config.readConfig()

# openai.api_key = config.getPkApiKey()
openai.api_base = 'https://api.pawan.krd/v1'


def get_chatgpt_answer(question):
    try:
        response = OpenAI(api_key=config.getRandApiKey()).chat.completions.create(
            model=config.getGPTModel(),
            response_format={"type": "json_object"},
            temperature=random.random(),
            top_p=random.random(),
            seed=random.randint(100, 300),
            messages=[
                {"role": "system",
                 "content": "You are answering a questionnaire that aims to understand your shopping habits, preferences, and attitudes towards technology-driven enhancements to the in-store shopping experience. Your answers should output into a JSON with key-pair values with property name enclosed in double quotes. You can use numbers for the keys."},
                {"role": "user", "content": f"{question}"}
            ]
        )
        json_data = ast.literal_eval(json.dumps(response.choices[0].message.content))
        json_response = json.loads(json_data)
        # first_key = next(iter(json_response.keys()))
        keys = list(json_response.keys())
        random_key = random.choice(keys)

        print(f"{question}:{json_response}")
        answer = json_response[random_key]
        print(f"Chosen: {answer}")

        # choices = [True, False]
        # pp = random.choice(choices)
        # if pp is True:
        #     return paraphrase_answer(answer)
        # else:
        #     return no_paraphrase_answer(answer)
        return no_paraphrase_answer(answer)


    except openai.RateLimitError as e:
        print(f"Rate limit reached, trying in 20s = {e.message}")
        sleep(21)
        get_chatgpt_answer(question)


def paraphrase_answer(answer):
    try:
        response = OpenAI(api_key=config.getRandApiKey()).chat.completions.create(
            model=config.getGPTModel(),
            response_format={"type": "json_object"},
            temperature=random.random(),
            top_p=random.random(),
            seed=random.randint(100, 300),
            messages=[
                {"role": "system",
                 "content": "You should paraphase the given text, you should not change any information or facts. You can make the text sound a little informal. You should also output into a JSON."},
                {"role": "user", "content": f"{answer}"}
            ]
        )
        json_response = json.loads(response.choices[0].message.content)
        # json_response = json.loads(json_data)

        first_key = next(iter(json_response.keys()))
        return json_response[first_key]

    except openai.RateLimitError:
        print(f"[PP] Rate limit reached, trying in 20s")
        sleep(21)
        paraphrase_answer(answer)


def no_paraphrase_answer(answer):
    return answer
