import json
import random
import openai
from openai import OpenAI
from config import Config
from time import sleep

config = Config('config.ini')
config.readConfig()


def get_chatgpt_answer(question):
    try:
        response = OpenAI(api_key=config.getRandApiKey()).chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={"type": "json_object"},
            temperature=random.random(),
            top_p=random.random(),
            seed=random.randint(100, 300),
            messages=[
                {"role": "system",
                 "content": "You are answering a questionnaire that aims to understand your shopping habits, preferences, and attitudes towards technology-driven enhancements to the in-store shopping experience. Your answers should output into a JSON with key-pair values. You can use numbers for the keys."},
                {"role": "user", "content": f"{question}"}
            ]
        )
        json_response = json.loads(response.choices[0].message.content)
        # first_key = next(iter(json_response.keys()))
        keys = list(json_response.keys())
        random_key = random.choice(keys)

        print(f"{question}:{json_response}")
        answer = json_response[random_key]
        choices = [True, False]
        pp = random.choice(choices)
        if pp is True:
            return paraphrase_answer(answer)
        else:
            return no_paraphrase_answer(answer)

        # paraphrased_answer = paraphrase_answer(answer)


    except openai.RateLimitError:
        print(f"Rate limit reached, trying in 20s")
        sleep(21)
        get_chatgpt_answer(question)


def paraphrase_answer(answer):
    try:
        response = OpenAI(api_key=config.getRandApiKey()).chat.completions.create(
            model="gpt-3.5-turbo",
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
        first_key = next(iter(json_response.keys()))
        return json_response[first_key]

    except openai.RateLimitError:
        print(f"[PP] Rate limit reached, trying in 20s")
        sleep(21)
        paraphrase_answer(answer)


def no_paraphrase_answer(answer):
    return answer
