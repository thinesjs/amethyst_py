import random
import requests
from time import time
from urllib.parse import quote
from chatgpt import get_chatgpt_answer
from config import Config
from utils import get_random_name

config = Config('config.ini')
config.readConfig()
base_url = config.getFormsURL()

# GLOBAL GFORMS OPTIONS
linear_scale_options = [
    ["1"],
    ["3"], ["4"]
]

linear_scale_options1 = [

    ["4"], ["5"]
]

boolean_options = [
    ["Yes"], ["No"]
]


def main():
    # QUESTIONS
    answer_list = []
    start_answering_time = time()
    # Q1
    age_list = [
        ["20-29"], ["30-39"], ["40-49"]
    ]

    marital_list = [
        ["Single"], ["Married"], ["Seperated"]
    ]

    edu_list = [
        ["High+School+Graduate"], ["Bachelor's+Degree"], ["Postgraduate+Education"], ["Prefer+Not+To+Say"]
    ]
    # answer_list.append([None, 1013725562, random.choice(gender_list), 0])

    employment_list = [
        ["Employed"], ["Unemployed"], ["Student"]
    ]

    deaf_list = [
        ["Since+Birth"], ["Early+Childhood"], ["Prefer+Not"]
    ]

    environments1_list = [
        ["Group+Discussions"], ["Rapid+Conversation+with+Individual"], ["Rapid+Conversation+with+Individual"],
        ["Outdoor+Events"], ["Telephone+Interactions"], ["Workplace+Communication"]
    ]

    clarification_list = [
        ["Always"], ["Sometimes"], ["Rarely"], ["Never"]

    ]

    answer_list.append([None, 648519647, [f"{get_random_name().replace(' ', '+')}"], 0])
    answer_list.append([None, 132767898, random.choice(age_list), 0])
    answer_list.append([None, 1284074989, random.choice(marital_list), 0])
    answer_list.append([None, 1115636542, random.choice(edu_list), 0])
    answer_list.append([None, 50834187, random.choice(employment_list), 0])
    answer_list.append([None, 1976281572, random.choice(deaf_list), 0])
    answer_list.append([None, 1540937920, random.choice(boolean_options), 0])
    answer_list.append([None, 241463143, random.choice(linear_scale_options), 0])
    answer_list.append([None, 1663623869, random.choice(environments1_list), 0])
    answer_list.append([None, 1822225394, random.choice(clarification_list), 0])
    answer_list.append([None, 503887739, random.choice(linear_scale_options), 0])
    answer_list.append([None, 2000406878, random.choice(linear_scale_options), 0])
    answer_list.append([None, 675323482, random.choice(boolean_options), 0])
    answer_list.append([None, 831942799, random.choice(boolean_options), 0])
    answer_list.append([None, 2086615887, random.choice(linear_scale_options1), 0])
    answer_list.append([None, 215257176, random.choice(linear_scale_options), 0])
    answer_list.append([None, 800466173, random.choice(boolean_options), 0])
    answer_list.append([None, 783743958, random.choice(boolean_options), 0])
    answer_list.append([None, 333921335, random.choice(boolean_options), 0])

    end_answering_time = time()

    # LAST QUESTION
    last_list = {
        'entry.412382091': 'Yes',
        'entry.412382091_sentinel': '',
    }

    string_list = str([answer_list, None, '-3024905695224604276']).replace('None', 'null').replace(' ', '')

    gforms_payload = {
        **last_list,
        'fvv': '1',
        'partialResponse': quote(string_list, safe='+'),
        'pageHistory': quote("0,1,2,3,4", safe=''),
        'fbzx': '-3024905695224604276',
        'submissionTimestamp': int(time()),
    }

    formatted_payload = "&".join([f"{key}={value}" for key, value in gforms_payload.items()])

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': '266', KIV:: check if needed
        'Host': 'docs.google.com',
        'Origin': 'https://docs.google.com',
        'Connection': 'keep-alive',
        'Referer': f'{base_url}/formResponse',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    run = requests.post(f'{base_url}/formResponse', headers=headers, data=formatted_payload, timeout=15)

    execution_time_ms = (end_answering_time - start_answering_time) * 1000  # Convert to milliseconds
    formatted_execution_time = "{:.1f}ms".format(execution_time_ms)
    print(f"Execution completed in {formatted_execution_time} with HTTP status {run.status_code}")


class AmethystPy2(object):
    def __init__(self):
        attempts = int(config.getMaxAttempt())
        # input(f"Press ENTER to submit a response:")
        try:
            for x in range(attempts):
                print(f"Execution started for {x + 1} response...")
                main()
            # print(f"Execution started...")
            # main()
            # print(f"Execution completed!")
            # exit()
        except KeyboardInterrupt:
            print("You have forcefully stopped the program.")
