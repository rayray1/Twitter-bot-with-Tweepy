import tweepy

consumer_key = '#'
consumer_secret = '#'
access_token = '#'
access_token_secret = '#'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# check if working fine
user = api.me()
print (user.name)
print(user.location)

# loop through followers and follow
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone that is following " + user.name)

# main function
def mainFunction():
    search = 'Keyword'
    numberofTweets = "Number of tweets you wish to interact with"

    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.favourite()
            tweet.retweet()
            print('Favourited and Retweeted tweet')

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

    phrase = "What you would like your response tweet to say"
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
            print ("Replied with " + phrase)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
