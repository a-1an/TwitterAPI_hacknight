import os
import ast
import tweepy
check=os.path.isfile("./connection.txt")  #check if file exists
print(check)
if check:
    with open("connection.txt", "r") as file:
        contents=file.read()
        config=ast.literal_eval(contents) #converting text to dictionary 
        print(config)
if check==False:
    host=input("ENTER HOST")
    user=input("ENTER USERNAME")
    password=input("ENTER PASSWORD")
    database=input("ENTER DATABASE")
    config = {"consumer_key": host,
                "consumer_secret": user,
                "access_token": password,
                "access_token_secret": database}

    if db.is_connected():
        printc(green("\n successfully connected, GOOD to GO"))
        with open("connection.txt","w") as file:
            file.write(str(dbconfig))
    else:
        print("error")

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")