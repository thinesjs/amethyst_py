import random
import requests
from time import time
from urllib.parse import quote
from chatgpt import getchatgptanswer
from config import Config

config = Config('config.ini')
config.readConfig()

base_url = config.getFormsURL()

# GLOBAL GFORMS OPTIONS
linear_scale_options = [
    ["1"], ["2"], ["3"], ["4"], ["5"]
]
boolean_options = [
    ["Yes"], ["No"]
]

# QUESTIONS
answer_list = []

# Q1
age_list = [
    ["17+years+old+or+younger"], ["18+-+24+years+old"], ["25+-+34+years+old"], ["35+-+44+years+old"],
    ["45+-+54+years+old"], ["55+years+old+or+older"]
]
answer_list.append([None, 2032264928, random.choice(age_list), 0])

# Q2
gender_list = [
    ["Male"], ["Female"],  # ["Prefer+not+to+say"]
]
answer_list.append([None, 1013725562, random.choice(gender_list), 0])

# Q3 - How often do you shop at brick-and-mortar/offline/retail stores compared to online stores?
answer_list.append([None, 1092006797, random.choice(linear_scale_options), 0])

# Q4 - What factors influence your decision to shop at a brick-and-mortar store?
q4_response = getchatgptanswer("What factors influence your decision to shop at a brick-and-mortar store?").replace(' ', '+')
answer_list.append([None, 1703416426, [f"{q4_response}"], 0])
# Q5 - What types of products do you prefer to purchase in-store rather than online?
q5_response = getchatgptanswer("What types of products do you prefer to purchase in-store rather than online?").replace(' ', '+')
answer_list.append([None, 1508710175, [f"{q5_response}"], 0])
# Q6 - Have you ever received personalised recommendations or greetings from a brick-and-mortar store?
q6_choice = random.choice(boolean_options)
answer_list.append([None, 1894295135, q6_choice, 0])
# Q7 - If yes, how did you feel about the personalised experience? Did it enhance your shopping experience?
if q6_choice == '["Yes"]':
    q7_response = getchatgptanswer("How did you feel about receiving personalised experience in the past? Did it enhance your shopping experience?").replace(' ', '+')
else:
    q7_response = getchatgptanswer("How do you feel about receiving personalised experience in the future? Will it enhance your shopping experience?").replace(' ', '+')
answer_list.append([None, 854436901, [f"{q7_response}"], 0])
# Q8 - How comfortable are you with the use of facial recognition technology in brick-and-mortar stores?
q8_choice = random.choice(linear_scale_options)
answer_list.append([None, 1499900330, q8_choice, 0])
# Q9 - What concerns, if you are not comfortable, do you have about privacy and data security related to facial recognition?
if q8_choice == '["1"]' or '["2"]':
    q9_response = getchatgptanswer("What concerns do you have about privacy and data security related to facial recognition that will make you to not participate in this proposed solution?").replace(' ', '+')
else:
    q9_response = getchatgptanswer("What concerns do you have about privacy and data security related to facial recognition?").replace(' ', '+')
answer_list.append([None, 1935879695, [f"{q9_response}"], 0])
# Q10 - Would you appreciate receiving personalised greetings or recommendations based on your previous shopping history?
answer_list.append([None, 1051691068, random.choice(boolean_options), 0])
# Q11 - What types of personalised recommendations would you find most valuable?
q11_response = getchatgptanswer("What types of products do you prefer to purchase in-store rather than online?").replace(' ', '+')
answer_list.append([None, 26266239, [f"{q11_response}"], 0])
# Q12 - Are you currently enrolled in any loyalty programs offered by brick-and-mortar stores?
answer_list.append([None, 732149606, random.choice(boolean_options), 0])
# Q13 - What incentives or rewards would encourage you to participate in a loyalty program?
q13_response = getchatgptanswer("What incentives or rewards would encourage you to participate in a loyalty program?").replace(' ', '+')
answer_list.append([None, 1051389942, [f"{q13_response}"], 0])
# Q14 - How likely are you to return to a store that offers personalised greetings, recommendations, or rewards?
answer_list.append([None, 323706928, random.choice(linear_scale_options), 0])
# Q15 - Do you have any additional suggestions or feedback on how brick-and-mortar stores can improve the shopping experience through technology?
q15_response = getchatgptanswer("Do you have any additional suggestions or feedback on how brick-and-mortar stores can improve the shopping experience through technology?").replace(' ', '+')
answer_list.append([None, 223764250, [f"{q15_response}"], 0])
# Q16 - What factors influence your decision to shop at a particular brick-and-mortar store?
q16_response = getchatgptanswer("What factors influence your decision to shop at a particular brick-and-mortar store? (That one offline shop that you always go to)").replace(' ', '+')
answer_list.append([None, 1376724546, [f"{q16_response}"], 0])
# Q17 - How important is customer service in your overall shopping experience?
answer_list.append([None, 1056742149, random.choice(linear_scale_options), 0])
# Q18 - Do you typically use mobile applications while shopping in-store?
answer_list.append([None, 1613996379, random.choice(boolean_options), 0])
# Q19- Would you be willing to download and use a mobile application from your favourite brick-and-mortar store?
answer_list.append([None, 577038100, random.choice(boolean_options), 0])
# Q20- Is there anything else you would like to share about your shopping habits, preferences, or experiences?
q20_response = getchatgptanswer("Is there anything else you would like to share about your shopping habits, preferences, or experiences?").replace(' ', '+')
answer_list.append([None, 368095154, [f"{q20_response}"], 0])

# LAST QUESTION
last_list = {
    'entry.1618586629': 'Yes',
    'entry.1618586629_sentinel': '',
}

string_list = str([answer_list, None, '-4390342051369665498']).replace('None', 'null').replace(' ', '')

gforms_payload = {
    **last_list,
    'fvv': '1',
    'partialResponse': quote(string_list, safe='+'),
    'pageHistory': quote("0,1,2,3,4,5,6,7,8,9,10,11", safe=''),
    'fbzx': '-4390342051369665498',
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
print(run.status_code)

# class AmethystPy(object):
#     def __init__(self):
#         print(f"Scanning for QR every  seconds...")
#         try:
#             print(f"Scanning for QR every seconds...")
#             # check_qr(capture_window())
#         except KeyboardInterrupt:
#             print("You have forcefully stopped the program.")
