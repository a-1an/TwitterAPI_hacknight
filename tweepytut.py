import tweepy,os,ast
from dotenv import load_dotenv

load_dotenv()


client = tweepy.Client(bearer_token=os.environ.get("bearer_token"),
                       consumer_key=os.environ.get('consumer_key'),
                       consumer_secret=os.environ.get('consumer_secret'),
                       access_token=os.environ.get('access_token'),
                       access_token_secret=os.environ.get('access_token_secret'))

# Replace the text with whatever you want to Tweet about
check=os.path.isfile("./tweet_id.txt")  #check if file exists
print(check)
if check:
    with open("./tweet_id.txt", "r") as file:
        contents=file.read()
        id_list=ast.literal_eval(contents) #converting text to dictionary 
        print(id_list)
if check==False:
    id_list=[]
    with open("./tweet_id.txt","w") as file:
        file.write(str(id_list))
response = client.create_tweet(text='he55jhjihuihuiyguy55hi')
id=response.data['id']
id_list.append(id)
print(id_list)
with open("./tweet_id.txt","w") as file:
        file.write(str(id_list))
tweets = client.get_tweets(ids=response.data['id'])
for tweet in tweets.data:
    print(tweet)                                                                      

#print(response) 
#print(l)       
