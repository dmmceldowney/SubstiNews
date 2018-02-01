import requests
import json
import wordSwap
from data import news_key

dictionary = {
    "WITNESSES" : "These Dudes I Know",
    "ALLEGEDLY" : "Kinda Probably",
    "NEW STUDY" : "Tumblr Post",
    "REBUILD" : "Avenge",
    "SPACE" : "SPAAAAACE",
    "GOOGLE GLASS" : "Virtual Boy",
    "SMARTPHONE" : "Pokedex",
    "ELECTRIC" : "Atomic",
    "SENATOR" : "Elf-Lord",
    "CAT" : "Cat",
    "ELECTION" : "Eating Contest",
    "CONGRESSIONAL LEADERS" : "River Spirits",
    "HOMELAND SECURITY" : "Homestar Runner",
    "COULD NOT BE REACHED FOR COMMENT" : "Is Guilty and Everyone Knows It",
    "APPLE" : "Hipster-Microsoft",
    "MICROSOFT" : "Successful-Apple",
    "DRUGS" : "Happy Pills",
    "GOOGLE" : "Future Skynet",
    "COMCAST" : "Greedy Jerks",
    "FACEBOOK" : "Big Brother",
    "TWITTER" : "More-vain Facebook",
    "INSTAGRAM" : "Sepia-Facebook",
    "DEBATE" : "Dance-Off",
    "SELF DRIVING" : "Uncontrollably Swerving",
    "SELF-DRIVING" : "Uncontrollably Swerving",
    "POLL" : "Psychic Reading",
    "CANDIDATE" : "Airbender",
    "DRONE" : "Dog",
    "VOWS TO" : "Probably Won't",
    "AT LARGE" : "Very Large",
    "SUCCESSFULLY" : "Suddenly",
    "EXPANDS" : "Physically Expands",
    "AN UNKNOWN NUMBER" : "Like Hundreds",
    "FRONT RUNNER" : "Blade Runner",
    "GLOBAL" : "Spherical",
    "YEARS" : "Minutes",
    "MINUTES" : "Years",
    "NO INDICATION" : "Lots of Signs",
    "URGED RESTRAINT BY" : "Drunkenly Egged On",
    "HORSEPOWER" : "Tons of Horsemeat",
    "GAFFE" : "Magic Spell",
    "ANCIENT" : "Haunted",
    "STAR-STUDDED" : "Blood-Soaked",
    "SUBWAY SYSTEM" : "Tunnels I Found",
    "SURPRISING" : "Surprising (But Not To Me)",
    "TENSION" : "Sexual Tension",
    "CAUTIOUSLY OPTIMISTIC" : "Delusional",
    "DOCTOR WHO" : "The Big Bang Theory",
    "WIN VOTES" : "Find Pokemon",
    "EMAIL" : "Poem",
    "FACEBOOK POST" : "Poem",
    "TWEET" : "Poem",
    "FACEBOOK CEO" : "This Guy",
    "LATEST" : "Final",
    "DISRUPT" : "Destroy",
    "MEETING" : "Menage a Trois",
    "SCIENTISTS" : "Channing Tatum and His Friends"
}

news_sites = {
    "abc-news-au",
    "al-jazeera-english",
    "ars-technica",
    "associated-press",
    "bbc-news",
    "bbc-sport",
    "bild",
    "bloomberg",
    "breitbart-news",
    "business-insider",
    "business-insider-uk",
    "buzzfeed",
    "cnbc",
    "cnn",
    "daily-mail",
    "engadget",
    "entertainment-weekly",
    "espn",
    "espn-cric-info",
    "financial-times",
    "focus",
    "fortune",
    "google-news",
    "hacker-news",
    "ign",
    "independent",
    "newsweek",
    "polygon",
    "reuters",
    "techcrunch",
    "techradar",
    "the-economist",
    "the-huffington-post",
    "the-wall-street-journal",
    "the-washington-post"
}

def getHeadline():
    for source in wordSwap.news_sites:
        url = 'https://newsapi.org/v1/articles?source=' + source + '&sortBy=top&apiKey=' + news_key
        # get the request data
        req = requests.get(url)
        # puts the headline into a json dictionary
        json_data = json.loads(req.text)
        # get data from specific area
        articles = json_data.get('articles')
        for article in articles:
            title = article['title']
            art_url = article['url']
            article_changed = 0
            headline = title.split(" ")
            newHeadline = ""
            c = 0
            c_n = 1
            while c < len(headline):
                if c_n < len(headline):
                    combo = (headline[c] + " " + headline[c_n])
                else:
                    combo = " "
                if combo.upper() in wordSwap.dictionary:
                    newHeadline += " " + wordSwap.dictionary[combo.upper()]
                    c += 1
                    c_n += 1
                    article_changed = 1
                elif headline[c].upper() in wordSwap.dictionary:
                    article_changed = 1

                    newHeadline += " " + wordSwap.dictionary[headline[c].upper()]
                else:
                    newHeadline += " " + headline[c]
                c += 1
                if (c_n < len(headline)):
                    c_n += 1
            if article_changed == 1:
                array = []
                array.append(newHeadline[1:])
                array.append(art_url)
                return array
    return "no change"