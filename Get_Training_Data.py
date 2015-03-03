import csv

# Function to read csv file in
def read_file(filename):
    result = []
    with open(filename, 'r',encoding = "utf-8") as f:
        for line in f:
            line = line[:-1] # removing the newline character
            try:
                content, category = line.split(",")
                result.append([content,category])
            except ValueError:
                pass
            
    f.close()
    return result

# Function to remove duplicated data
def remove_duplicate(tweet_list):
    index = 0
    while(index != len(tweet_list)-1):
        tweet = tweet_list[index]
        if tweet in tweet_list[index+1:]:
            tweet_list.remove(tweet)
        else:
            index += 1
    return tweet_list

def clean_tweet(tweet_with_category):
    tweet,category = tweet_with_category[0],tweet_with_category[1]
    # Remove the RT(retweet) sign
    if "RT" in tweet:
        tweet = tweet.replace("RT ","")
    # Remove the @id notation
    while "@" in tweet:
        index1 = tweet.find("@")
        index2 = tweet[index1:].find(" ")
        # Detect the case when the @id is at the end
        if index2 == -1:
            tweet = tweet[:index1]
        else:
            tweet = tweet[:index1] + tweet[index1+index2+1:]
    # Remove the link
    counter = 0 # Used to break
    while "/" in tweet:
        counter = counter + 1
        if counter > 5:
            break
        index3 = tweet.find("/")
        index4 = tweet[index3:].find(" ")
        index5 = index3
        while tweet[index5]!=" ":
            index5 = index5 - 1
            if index5 == 0:
                break
        # Detect the case when the link is at the end
        if index4 == -1:
            tweet = tweet[:index3]
        else:
            tweet = tweet[:index5] + tweet[index3+index4:]
    # Remove the hash
    tweet = tweet.replace("#","")
    return [tweet,category]

def output_csv(tweet_list,filename):
    
    filepointer =  open(filename,"a",encoding = 'utf-8')
    writer = csv.writer(filepointer)

    result  = []
    for tweet_with_category in tweet_list:
        try:
            new_tweet_with_category = clean_tweet(tweet_with_category)
            result.append(new_tweet_with_category)
        except UnicodeEncodeError:
            continue
        except IndexError:
            continue

    final_result = remove_duplicate(result)[:24635]
    print(len(final_result))
        
    writer.writerows(final_result)        
    filepointer.close()

automobile = read_file("automobile.csv")
output_csv(automobile,"training_data.csv")

book = read_file("book.csv")
output_csv(book,"training_data.csv")

education = read_file("education.csv")
output_csv(education,"training_data.csv")

fashion = read_file("fashion.csv")
output_csv(fashion,"training_data.csv")

finance = read_file("finance.csv")
output_csv(finance,"training_data.csv")

food = read_file("food.csv")
output_csv(food,"training_data.csv")

movie = read_file("movie.csv")
output_csv(movie,"training_data.csv")

music = read_file("music.csv")
output_csv(music,"training_data.csv")

politics = read_file("politics.csv")
output_csv(politics,"training_data.csv")

sports = read_file("sports.csv")
output_csv(sports,"training_data.csv")

technology = read_file("technology.csv")
output_csv(technology,"training_data.csv")


    
