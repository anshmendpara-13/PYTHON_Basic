
# Akhbaar padhke sunaao
import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':

    # speak("neev is good ")
    speak("hi khahur ")
    speak("News for today.. Lets begin")
    print("1. technology ")
    print("2. bussiness ")
    print("3. entertentment ")
    print("4. all types")
    x = int(input("Enter the you choice :- "))

    # url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b1ffb21e77cb4f3f9ba52611d21e7a85"
while True:
    if x == 1:
        url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b1ffb21e77cb4f3f9ba52611d21e7a85"
    elif x == 2:
        url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b1ffb21e77cb4f3f9ba52611d21e7a85"
    elif x == 3:
        url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=b1ffb21e77cb4f3f9ba52611d21e7a85"
    elif x == 4:
        url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=b1ffb21e77cb4f3f9ba52611d21e7a85"
    else:
        print("Enter the right choice")

    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    i=1
    for article in arts:
        print(i,":->",article['title'])
        speak(article['title'])
        print("url for read more :-",article['url'])
        print("picture :-",article['urlToImage'])
        i=i+1
        print("\n")

        # speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")
    # print("URL link :-","https://newsapi.org/s/india-entertainment-news-api")