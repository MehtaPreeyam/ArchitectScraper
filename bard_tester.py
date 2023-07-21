from bardapi import Bard
import requests
import re

def get_startups(telehealth_startups: list):
    for i in range(0, len(telehealth_startups), 2):
        startup = telehealth_startups[i]
        match = re.search(pattern, startup)
        if match:
            result = match.group(1)
            startups.add(result)
        else:
            print("No match found.")



BARD_TOKEN = 'YwgWsmIvjPHHp7GEKti6pbRRl5y1iriGDcWdCC0lmxMA1a-9k5TCw60I388oi9SWN82usA.'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", BARD_TOKEN) 

pattern = r"\*\*\s*(.*?)\s*\*\*"

startups = set()

bard = Bard(token=BARD_TOKEN, session=session, timeout=30)

telehealth_startups = bard.get_answer("Can you give me the top 30 Telehealth Startups in the USA?")['content'].split("\n")

get_startups(telehealth_startups)

# Continued conversation without set new session
telehealth_startups = bard.get_answer("Can you give me 50 more unique ones?")['content']

get_startups(telehealth_startups)

print(startups)
