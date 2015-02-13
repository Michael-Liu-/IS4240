import tweepy
import csv


# Twitter Application Details

consumer_key1 = "jguhiszIMivXE5bRFgtLpUN7i"
consumer_secret1 = "zZYyTX0367lLJ0gsCTZSJclsp4agP2UdL382wVL9mbM7LurpnK"
access_token1 = "3000326876-FBOARSTXbS7dMvNBjgAdlDtko9YKOYdnLmHEWR5"
access_token_secret1 = "4spMIQK90MfOGiBsrvYisOvekUbUsTp3EsvbucPyYpJ3j"

consumer_key2 = "R68lzKZuvyFXdHQjvefHtkdSF"
consumer_secret2 = "SuW5jHZN7oBJtiLdar8yTlrzKjnIPlEwe454RT7g0iqQrenQxf"
access_token2 = "2851389240-lk1UKcVLQvX1FsgCfaiLTX6RFX2rZQ2yiEnqV0F"
access_token_secret2 = "DRZfBOcnkgSD1ic3F9OzFaRAzmC7fY6RYJMShup6LM1cO"

consumer_key3 = 'AEU51EcKXlQHvlGKCBU0Wwi7m'
consumer_secret3 = 'rNVackoWiRQCkCEIzyFbKRanmACSy7CFecKfWML29Aa8rbEaXS'
access_token3 = '2851389240-JxWsw0jbpUmL1fcFWo5nhAApwuDnxrCagRm1hzz'
access_token_secret3 = 'TKG2ykQqBx0MKcjWXxOmunvCWDu4NoRob1fV93mGljJXx'

consumer_key4 = 'ZItJk37oqYRIgMKC0iEJisq4W'
consumer_secret4 = 'ibhyYFbBdXSXM1RYpV3I2abk14GJSJ4jVoVqxBsMc6KdbE2sFz'
access_token4 = '2851389240-YeMTNWK6oMIF0g5j9SNheRVdFFZmG3RIf8Jg81w'
access_token_secret4 = 'uwiShA8kKcOenAvWVioTER9ZQ22P7cNRO9qxlZTzYxigY'

key1 = [consumer_key1,consumer_secret1,access_token1,access_token_secret1]
key2 = [consumer_key2,consumer_secret2,access_token2,access_token_secret2]
key3 = [consumer_key3,consumer_secret3,access_token3,access_token_secret3]
key4 = [consumer_key4,consumer_secret4,access_token4,access_token_secret4]
keys = [key1,key2,key3,key4]


# Create Authentication Object
def generate_api(keynumber,keys):
    key = keys[keynumber]
    consumer_key,consumer_secret,access_token,access_token_secret = key[0],key[1],key[2],key[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api



# Function to crawl data, username refers to the unique id (e.g.@TheEconomist),
# item_number refers to the number of tweets you want to crawl, common_pattern
# refers to the common pattern of the links in the tweets, like "econ.st/" for @The Economist
def crawl_data_username_item(api, username, item_number, common_pattern):
    result = []
    for item in tweepy.Cursor(api.user_timeline,username).items(item_number):
        cleaned_text = remove_http(item.text)
        cleaned_text = remove_link(cleaned_text,common_pattern)
        result.append(cleaned_text)
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


# Output the tweet_list related to particular category to a specific file
def output_csv(tweet_list,category,filename):
    
    # Filter out all the tweets with no length
    new_tweet_list = list(filter(lambda text: len(text) != 0,tweet_list))
    
    filepointer =  open(filename,"a",encoding = 'utf-8')
    writer = csv.writer(filepointer)

    result = []
    for tweet in new_tweet_list:
        # Remove all the "," and " " characters in the tweet and replace them with " "
        tweet = cleanse_tweet(tweet,',')
        tweet = cleanse_tweet(tweet,'\n')
        # Append new column category
        content = [tweet,category]
        result.append(content)
    
    writer.writerows(result)        
    filepointer.close()
        

# Twitter Accounts under Category Finance, Please use the twitter id, instead of Account name    
##account1,link_pattern1 = "TheEconomist","econ.st/" 
##account2,link_pattern2 = "FinancialTimes","on.ft.com/" 
##account3,link_pattern3 = "WSJ","on.wsj.com/" 
##account4,link_pattern4 = "TeleFinance","telegraph.co.uk/"
##account5,link_pattern5 = "ftfinancenews","on.ft.com/"
##account6,link_pattern6 = "ftchina","on.ft.com/"
##account7,link_pattern7 = "IMFNews","ow.ly/"
##account8,link_pattern8 = "federalreserve","usa.gov/"
##account9,link_pattern9 = "ecb","bit.ly/"
##account10,link_pattern10 = "eFinancialNews","efinancialnews.com/"

# Twitter Accounts under Category Fashion, Please use the twitter id, instead of Account name    
account1,link_pattern1 = "Fashionista_com","bit.ly/" 
account2,link_pattern2 = "TimesFashion","thetim.es/" 
account3,link_pattern3 = "glamour_fashion","glmr.me/" 
account4,link_pattern4 = "InStyle","trib.al/"
account5,link_pattern5 = "hm","hm.info/"
account6,link_pattern6 = "Forever21","bit.ly/"
account7,link_pattern7 = "Topman","tpmn.co/"
account8,link_pattern8 = "LouisVuitton","vuitton.lv/"
account9,link_pattern9 = "Abercrombie","bit.ly/"
account10,link_pattern10 = "Superdry","sdry.co/"

# Twitter Accounts under Category Electronics, Please use the twitter id, instead of Account name    
##account1,link_pattern1 = "google","goo.gl/" 
##account2,link_pattern2 = "applenws","bit.ly/" 
##account3,link_pattern3 = "Dropbox","bit.ly/" 
##account4,link_pattern4 = "fttechnews","on.ft.com/"
##account5,link_pattern5 = "ForbesTech","onforb.es/"
##account6,link_pattern6 = "guardiantech","d.gu.com/"
##account7,link_pattern7 = "SAI","read.bi/"
##account8,link_pattern8 = "CNET","cnet.co/"
##account9,link_pattern9 = "YahooTech","yhoo.it/"
##account10,link_pattern10 = "TechCrunch","tcrn.ch/"

# Twitter Accounts under Category Education, Please use the twitter id, instead of Account name    
##account1,link_pattern1 = "educationweek","blogs.edweek.org/" 
##account2,link_pattern2 = "usedgov","bit.ly/" 
##account3,link_pattern3 = "educationnation","bit.ly/" 
##account4,link_pattern4 = "USNewsEducation","ow.ly/"
##account5,link_pattern5 = "GoogleForEdu","goo.gl/"
##account6,link_pattern6 = "education","bit.yl/"
##account7,link_pattern7 = "edutopia","edut.to/"
##account8,link_pattern8 = "HuffPostEdu","huff.to/"
##account9,link_pattern9 = "USATeducation","bit.ly/"
##account10,link_pattern10 = "NEAToday","bit.ly/"

# Twitter Accounts under Category Book, Please use the twitter id, instead of Account name    
##account1,link_pattern1 = "GuardianBooks","gu.com/" 
##account2,link_pattern2 = "TwitterBooks",".com/" 
##account3,link_pattern3 = "PenguinUKBooks","po.st/" 
##account4,link_pattern4 = "nybooks","j.mp/"
##account5,link_pattern5 = "nytimesbooks","nyti.ms/"
##account6,link_pattern6 = "latimesbooks","lat.ms/"
##account7,link_pattern7 = "goodreads",".ly/"
##account8,link_pattern8 = "amazonbooks","amzn.to/"
##account9,link_pattern9 = "BNBuzz","oak.ctx.ly/"
##account10,link_pattern10 = "Powells","powells.us/"


pairs = [
    [account1,link_pattern1],
    [account2,link_pattern2],
    [account3,link_pattern3],
    [account4,link_pattern4],
    [account5,link_pattern5],
    [account6,link_pattern6],
    [account7,link_pattern7],
    [account8,link_pattern8],
    [account9,link_pattern9],
    [account10,link_pattern10]
    ]

# The final function, item_number refers to no. of tweets per account
def start_to_crawl(api,item_number,category,filename):
    for pair in pairs:
        account,link_pattern = pair[0],pair[1]
        result = crawl_data_username_item(api,account,item_number,link_pattern)
        output_csv(result,category,filename)
    return None


api = generate_api(0,keys)
start_to_crawl(api,3000,"Fashion","fashion.csv")
            


