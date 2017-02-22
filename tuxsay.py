import sys
import requests

def get_tuxsay(sentence):
    tux_say = requests.get("https://helloacm.com/api/cowsay/?msg=" + sentence + "&f=tux").json()
    tux_say = tux_say.split("\n")
    reply = ""
    for line in tux_say:
        reply += line + "\n"
    return reply

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python tuxsay.py \"Your sentence.\"")
    else:
        print(get_tuxsay(sys.argv[1]))