import ast
import json
import random

import g4f
import openai
from g4f.client import Client
from openai import OpenAI
from config import Config
from time import sleep

config = Config('config.ini')
config.readConfig()

def get_chatgpt_answer(question):
    try:
        client = Client()
        response = client.chat.completions.create(
            model=g4f.models.llama3_70b_instruct,
            response_format={"type": "json_object"},
            # temperature=random.random(),
            # top_p=random.random(),
            # seed=random.randint(100, 300),
            messages=[
                {"role": "system",
                 "content": "You are answering a questionnaire that aims to understand your UI preference for an mobile application that is designed for a park called Perdana Botanical Gardens located in Kuala Lumpur. Consider good implementations of HCI. Paraphrase the answers you come up with, it must be unique. Your answers should output into a JSON with key-pair values with property name enclosed in double quotes. You can use numbers for the keys. Response should be JSON object only and JSON parsable string. Dont add markdown styling and starting sentences"},
                {"role": "system",
                 "content": "Keep the answers as humanly possible. Keep it short because mostly human doesnt put in too much effort into answering surveys. Randomize the sentence not starting the sentence with lowercase letters to mimic the human-ness"},
                {"role": "system",
                 "content": "Keep the answers as humanly possible. To further make it humanly possible, avoid punctuations like 'users\'' or 'don\'t'. Just put it as 'users' or 'dont'"},
                {"role": "user", "content": f"{question}"}
            ]
        )
        # print(response)
        json_data = ast.literal_eval(json.dumps(response.choices[0].message.content))
        print(json_data)
        json_response = json.loads(json_data)
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


# def paraphrase_answer(answer):
#     try:
#         response = OpenAI(api_key=config.getRandApiKey(), base_url="http://localhost:3040/v1").chat.completions.create(
#             model=config.getGPTModel(),
#             response_format={"type": "json_object"},
#             temperature=random.random(),
#             top_p=random.random(),
#             seed=random.randint(100, 300),
#             messages=[
#                 {"role": "system",
#                  "content": "You should paraphase the given text, you should not change any information or facts. You can make the text sound a little informal. You should also output into a JSON. Response should be JSON parsable string. Dont add markdown "},
#                 {"role": "user", "content": f"{answer}"}
#             ]
#         )
#         json_response = json.loads(response.choices[0].message.content)
#         # json_response = json.loads(json_data)
#
#         first_key = next(iter(json_response.keys()))
#         return json_response[first_key]
#
#     except openai.RateLimitError:
#         print(f"[PP] Rate limit reached, trying in 20s")
#         sleep(21)
#         paraphrase_answer(answer)
#

def no_paraphrase_answer(answer):
    return answer