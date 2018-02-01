import wordSwap
import shorten
import tweet
import time

oldurls = []

def makePost():
    headline = "The British military made a subtle change before showing off its newest aircraft carrier — and avoided an awkward Magic Spell https://goo.gl/8J4rhV"
    article = wordSwap.getHeadline()
    headline = article[0]
    art_url = article[1]
    shorter = (shorten.shorten(art_url))
    headline = headline + "\n" + shorter
    while (len(headline) > 140) or art_url in oldurls:
        article = wordSwap.getHeadline()
        headline = article[0]
        art_url= article[1]
        shorter = (shorten.shorten(art_url))

        headline = headline + "\n" + shorter

    tweet.sendTweet(headline)
    # add article to the list
    oldurls.append(art_url)

#900 s between runs
while True:
    if len(oldurls) > 96:
        oldurls = []
    makePost()
    time.sleep(900)