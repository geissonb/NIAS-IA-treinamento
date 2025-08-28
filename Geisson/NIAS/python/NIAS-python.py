tweets = [
"Wow, what a great day today!! #sunshine",
"I feel sad about the things going on around us. #covid19",
"I'm really excited to learn Python with @JovianML #zerotopandas",
"This is a really nice song. #linkinpark",
"The Python programming language is useful for data science",
"Why do bad things happen to me?",
"Apple announces the release of the new iPhone 12. Fans are excited.",
"Spent my day with family!! #happy",
"Check out my blog post on common string operations in Python. #zerotopandas",
"Freecodecamp has great coding tutorials. #skillup"
]

happy_words = [
    'great',
    'excited',
    'happy',
    'nice',
    'wonderful',
    'amazing',
    'best',
    'good'
]

sad_words = [
    'sad',
    'bad',
    'tragic',
    'unhappy',
    'worst'
]

happy_tweet = []
sad_tweet = []

for tweet in tweets:
    verify = tweet.split()
    for v in verify:
        v = v.replace('!','').replace('#','').replace(',','').replace('.','')
        if v in happy_words:
            happy_tweet.append(tweet)
            break
        elif v in sad_words:
            sad_tweet.append(tweet)
            break

print(happy_tweet)
print(sad_tweet)