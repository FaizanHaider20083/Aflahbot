import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time

message_list = open("comment_list.txt",'a+')
                        
message_list.write('fhjkdhfkdsl')
                        
message_list.close()

reddit = praw.Reddit(client_id = 'BAG5nKlB9zIQwg',
client_secret = 'uXroeieha2oXN3ahK08IfpBz-0jVRg',
user_agent = 'console: message_bot 1.0',
username = 'onlykeyla',
password = '1233456')



def check_author(author):
    
    
    
    return 0
i = 50

subreddits = ['crypto']
while (i>0):
    for topic in subreddits:
        
        subreddit = reddit.subreddit(topic)
        for submission in subreddit.new(limit = 20):
            print("online")
            submission.comments.replace_more(limit = 0)
            for comment in submission.comments :
                author = str(comment.author)
                                
                if check_author(author) == 1 :
                    
                    continue
                else :
                    try:
                        print(comment.author)
                        #reddit.redditor(author).message('Check ', 'Mate')
                        
                        print("Message sent")
                                    
                        message_list = open("comment_list.txt",'a+')
                        
                        message_list.write(comment.body + '\n')
                        
                        message_list.close()
                        continue
                    except praw.exceptions.APIException as e:
                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                            print("Lol this user has a whitelist, there is no way to message them, giving up")

    #time.sleep(600)

