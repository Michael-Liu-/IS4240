import tweepy
import csv


# Twitter Application Details

##consumer_key = "jguhiszIMivXE5bRFgtLpUN7i"
##consumer_secret = "zZYyTX0367lLJ0gsCTZSJclsp4agP2UdL382wVL9mbM7LurpnK"
##access_token = "3000326876-FBOARSTXbS7dMvNBjgAdlDtko9YKOYdnLmHEWR5"
##access_token_secret = "4spMIQK90MfOGiBsrvYisOvekUbUsTp3EsvbucPyYpJ3j"

consumer_key = 'AEU51EcKXlQHvlGKCBU0Wwi7m'
consumer_secret = 'rNVackoWiRQCkCEIzyFbKRanmACSy7CFecKfWML29Aa8rbEaXS'
access_token = '2851389240-JxWsw0jbpUmL1fcFWo5nhAApwuDnxrCagRm1hzz'
access_token_secret = 'TKG2ykQqBx0MKcjWXxOmunvCWDu4NoRob1fV93mGljJXx'


# Create Authentication Object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



# Function to crawl data, userlist refers to a list of unique id (e.g.@TheEconomist) of users,
# item_number refers to the number of tweets you want to crawl
def crawl_data_username_item(userlist, item_number):
    result = []
    for user in userlist: #The list must be the unique twitter id, not account name
        for item in tweepy.Cursor(api.user_timeline,user).items(item_number):
            # Remove all the "," and " " characters in the tweet and replace them with " "
            tweet = remove_http(item.text)
            tweet = cleanse_tweet(tweet,',')
            tweet = cleanse_tweet(tweet,'\n')
            # Filter out all the tweet with no length
            if len(tweet) == 0:
                pass
            else:
                content = [tweet,user]
                result.append(content)
    return result
        

# Remove url keywords of the tweets (Assuming the https are placed at the end of the text)
def remove_http(text):
    if not "http" in text:
        return text
    else:
        return text[:text.find("http")]


# Remove links within the tweets, e.g. econ.st.XX for tweets by TheEconomist
def remove_link(text,common_pattern):
    if not common_pattern in text:
        return text
    else:
        return text[:text.find(common_pattern)]
    
    

# Replace the particular character by " ", in case of multiple "," and "\n" in tweet 
def cleanse_tweet(text,character):
    while character in text:
        length = len(text)
        index = text.find(character)
        text = text[:index] + " " + text[index+1:]
    return text


# Output the tweet_list to a specific file
def output_csv(tweet_list,filename):
    
    filepointer =  open(filename,"a",encoding = 'utf-8')
    writer = csv.writer(filepointer)    
    writer.writerows(tweet_list)        
    filepointer.close()
        


# The final function, item_number refers to no. of tweets per account
def start_to_crawl(userlist,item_number):
    result = crawl_data_username_item(userlist,item_number)
    output_csv(result,category,filename)
    return None


# Uncomment the following line to run
start_to_crawl(userlist,"user_tweet.csv")


