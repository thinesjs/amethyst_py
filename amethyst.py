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
    # ["1"],
    ["2"],
    # ["3"],
    # ["4"], ["5"]
]
boolean_options = [
    # ["Yes"],
    ["No"],
    # ["Maybe"]
]


def main(name):
    # QUESTIONS
    answer_list = []
    start_answering_time = time()

    # Q0
    # name = get_random_name()
    answer_list.append([None, 1670562836, name, 0])

    # Q1
    q1 = [
        ["18-23"], ["24-30"],
        # ["30-40"],
        # ["40+"],
    ]
    answer_list.append([None, 645209432, random.choice(q1), 0])

    # Q2
    q2 = [
        ["Secondary"], ["Diploma/Foundation"], ["Bachelors+Degree"]
    ]
    answer_list.append([None, 367474266, random.choice(q2), 0])

    # Q3
    q3 = [
        ["Chinese"],
        ["Malay"],
        ["English"],
        # ["Tamil"]
    ]
    answer_list.append([None, 959684976, random.choice(q3), 0])

    # Q4
    q4 = [
        # ["Student"],
        # ["Unemployed"],
        ["Employed+full-time"], ["Employed+part-time"]
    ]
    answer_list.append([None, 2093334470, random.choice(q4), 0])

    # Q5
    answer_list.append([None, 2113521328, random.choice(linear_scale_options), 0])

    # Q6
    q6 = [
        ["Leisure+and+relaxation"],
        ["Exercise+and+fitness"],
        ["Educational+purposes"],
        ["Social+activities"],
        ["Events+or+functions"],
        ["Photography"]
    ]
    selected_options = random.sample(q6, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 1181954475, flattened_selected_options, 0])

    # Q7
    q7 = [
        ["Social+media"],
        ["Perdana+Botanical+Garden's+official+website"],
        ["Friends+or+family"],
        ["Local+newspapers+or+magazines"]
    ]
    selected_options = random.sample(q7, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 1775914105, flattened_selected_options, 0])

    # Q8
    q8 = [
        ["Directions+to+a+destination"],
        ["Real+time+location"],
        ["Points+of+interest"],
        ["Interactive+Guide"],
        ["Alerts+of+issues+in+the+park"],
        ["Reviews+and+photo+sharing"]
    ]

    selected_options = random.sample(q8, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 108529918, flattened_selected_options, 0])

    # Q9
    q9 = [
        ["Physical+maps"],
        ["Asking+staff+or+other+visitors"],
        ["Mobile+phone+GPS"]
    ]

    selected_options = random.sample(q9, random.randint(2, 3))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 1255921539, flattened_selected_options, 0])

    # Q10
    answer_list.append([None, 1107609351, random.choice(boolean_options), 0])

    # Q11
    q11 = [
        ["Interactive+map"],
        ["Points+of+interest+markers"],
        ["Walking+route+suggestions"],
        ["Accessibility+information"],
        ["Real-time+location+tracking"]
    ]

    selected_options = random.sample(q11, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 267521905, flattened_selected_options, 0])

    # Q12
    answer_list.append([None, 1416352018, random.choice(linear_scale_options), 0])

    # Q13 - What incentives or rewards would encourage you to participate in a loyalty program?
    q13 = [
        ["Upcoming+events"],
        ["Plant+and+wildlife+information"],
        ["Maintenance+updates"],
        ["Visitor+tips"],
        ["Historical+facts"]
    ]

    selected_options = random.sample(q13, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 186827964, flattened_selected_options, 0])

    # Q14
    answer_list.append([None, 136187744, random.choice(boolean_options), 0])

    # Q15
    answer_list.append([None, 1585386381, random.choice(linear_scale_options), 0])

    # Q16
    answer_list.append([None, 1223738549, random.choice(boolean_options), 0])

    # Q17
    answer_list.append([None, 313300307, random.choice(linear_scale_options), 0])

    # # Q18
    q18 = [
        ["Availability+calendar"],
        ["Pricing+information"],
        ["Online+payment+options"],
        ["Booking+confirmation"],
        ["Cancellation+and+refund+policies"]
    ]

    selected_options = random.sample(q18, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 256970674, flattened_selected_options, 0])

    # # Q19
    answer_list.append([None, 1568485898, random.choice(linear_scale_options), 0])
    #
    # # Q20
    q20 = [
        ["Light+theme"],
        ["Dark+theme"],
        ["High+contrast"],
        ["Nature-inspired+colors"]
    ]
    answer_list.append([None, 570495644, random.choice(q20), 0])

    # # Q21
    q21 = [
        ["Simple+and+minimalistic+designs"],
        ["Detailed+and+information-rich+designs"],
        ["Interactive+and+dynamic+designs"]
    ]

    selected_options = random.sample(q21, random.randint(2, 3))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 857331386, flattened_selected_options, 0])

    # Q22
    q22 = [
        ["Clear+and+readable+fonts"],
        ["Consistent+design+throughout+the+app"],
        ["Easy-to-find+buttons+and+links"],
        ["Visual+feedback+(e.g.,+button+animations+&+haptics)"],
        ["Quick+load+times"],
        ["Accessible+design+for+people+with+disabilities"]
    ]

    selected_options = random.sample(q22, random.randint(2, 4))
    flattened_selected_options = [item for sublist in selected_options for item in sublist]
    answer_list.append([None, 153947544, flattened_selected_options, 0])

    # Q23
    answer_list.append([None, 1494602752, random.choice(linear_scale_options), 0])

    # Q24
    # q24_response = get_chatgpt_answer(
    #     "Do you have any suggestions to improve the mobile application for Perdana Botanical Garden?").replace(' ',
    #                                                                                                            '+')
    try:
        q24_response = "no"
        q24_response_raw = get_chatgpt_answer(
            "Do you have any suggestions to improve the mobile application for Perdana Botanical Garden?").replace(' ',
                                                                                                                   '+')

        choices = [True, False]
        pp = random.choice(choices)
        if pp is True:
            q24_response_raw = q24_response_raw[0].lower() + q24_response_raw[1:]
            q24_response = q24_response_raw.replace(' ', '+')
        else:
            q24_response = q24_response_raw.replace(' ', '+')

    except:
        q24_response = "no".replace(' ', '+')

    end_answering_time = time()

    # LAST QUESTION
    last_list = {
        'entry.1799202772': q24_response,
        'entry.1799202772_sentinel': '',
    }

    string_list = str([answer_list, None, '-7271647148550707581']).replace('None', 'null').replace(' ', '')

    gforms_payload = {
        **last_list,
        'fvv': '1',
        'partialResponse': quote(string_list, safe='+'),
        'pageHistory': quote("0,1,2,3,4,5,6,7,8", safe=''),
        'fbzx': '5187982445727183517',
        'submissionTimestamp': int(time()),
    }

    formatted_payload = "&".join([f"{key}={value}" for key, value in gforms_payload.items()])

    print(formatted_payload)

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


class AmethystPy(object):
    def __init__(self):
        attempts = int(config.getMaxAttempt())
        # input(f"Press ENTER to submit a response:")
        try:

            names = [
                # ["azman+salleh"],
                # ["Nurul+Izzahh"],
                # ["Chan+wei+ling"],
                # ["Mohd+Ridzuan"],
                # ["lina+tan"],
                ["Khadijah"],
                ["Faizal+hamid+Abbidin"],
                ["Soo+Lee"],
                ["rosli+mahmood"]
            ]

            for x in names:
                # print(f"Execution started for {x + 1} response...")
                main(x)
            # print(f"Execution started...")
            # main()
            # print(f"Execution completed!")
            # exit()
        except KeyboardInterrupt:
            print("You have forcefully stopped the program.")
