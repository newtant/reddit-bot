import praw
import sys
import os
import time
import requests

def check_args():
    if len(sys.argv) < 2:
        print("Usage: python main.py $searchTerm $subredditName")
        sys.exit()
    else:
        return True

def login():
    print("Logging in...")
    return praw.Reddit('testBot', user_agent = "A test bot that parses new comments. v0.1")

def parse_comments(reddit, found_comments):
    for comment in reddit.subreddit(sys.argv[2]).comments(limit=25):
        if sys.argv[1] in comment.body.lower() and comment.id not in found_comments:
            print("Found " + sys.argv[1] + " in comment with ID " + comment.id + " written by /u/" + str(comment.author) + ".")
            found_comments.append(comment.id)
            comment.reply(get_cowsay())
            print("Replied successfully!")
            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

def already_replied_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        found_comments = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            found_comments = f.read()
            found_comments = found_comments.split("\n")
    return found_comments

def get_cowsay():
    sentence = "Regardless of your current choice of OS, you will always be welcome under my wings."
    tux_say = requests.get("https://helloacm.com/api/cowsay/?msg=" + sentence + "&f=tux").json()
    return tux_say

if __name__ == '__main__':
    if check_args():
        reddit = login()
        print("Logged in as /u/" + str(reddit.user.me()) + "! Starting to parse comments in /r/" + sys.argv[2] + "...")
        
        found_comments = already_replied_comments()

        while True:
            parse_comments(reddit, found_comments)
            print(found_comments)
            time.sleep(10)
