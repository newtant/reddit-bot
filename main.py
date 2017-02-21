import praw
import sys#, time

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
        if sys.argv[1] in comment.body and comment.id not in found_comments:
            print("Found " + sys.argv[1] + " in comment with ID " + comment.id + " written by /u/" + str(comment.author) + ".")
            found_comments.append(comment.id)
            #todo: figure out how to get the name of the comment author
            #this doesn't seem to be possible at first glance? what?
            #comment.reply("")

if __name__ == '__main__':
    if check_args():
        reddit = login()
        print("Logged in as /u/" + str(reddit.user.me()) + ". Starting to parse comments in /r/" + sys.argv[2] + "...")
        found_comments = []
        # while True:
        parse_comments(reddit, found_comments)
        #time.sleep(10)
