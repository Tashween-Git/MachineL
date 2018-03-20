from googlesearch import search
from urllib.request import urlopen as uReq
from urllib.error import URLError, HTTPError
import urllib
from bs4 import BeautifulSoup
#
# def google_scrape(url):
#     thepage = urllib.request.urlopen(url)
#     soup = BeautifulSoup(thepage, "html.parser")
#     return soup.title.text
#
# i = 1
# query = 'Le Meridien Mauritius'
# for url in search(query, num=1, stop=1):
#     a = google_scrape(url)
#     print(str(i) + ". " + a)
#     print(url)
#     print(" ")
#     i += 1

from urllib.request import Request, urlopen

def google_scrape(hotel_search):

    sites =["booking.com", "expedia", "agoda",""]
    total = 0

    score_array = []

    for x in range(4):
        print(x)
        print(hotel_search)

        url = "https://www.google.mu/search?q=" + hotel_search + sites[x] + "&ie=&oe="

        print(url)

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        thepage = urlopen(req).read()
        #uClient = uReq(url, data=None, timeout=None)
        #thepage = uClient.read()
        soup = BeautifulSoup(thepage, "html.parser")

        rating = soup.find("div", {"class": "slp"})

        rat_val = rating.text[10:13]
        rat_val = rat_val.replace("-","")

        #print(rating.text)
        if x == 0 or x == 2:
            #print(rating.text[10:13])
            x = rating.text[10:13]
            total += (float(rat_val)/2)
            score = float(rat_val)/2
            score_1 = ("%.1f" % score)
            print(score_1)
            score_array.append(score_1)
        elif x == 1:
            #print(rating.text[10:13])
            total += float(rat_val)
            score = float(rat_val)
            score_1 = ("%.1f" % score)
            print(score_1)
            score_array.append(score_1)
        else:
            #print("in else")
            rating = soup.find("span", {"class": "ul7Gbc"})
            #print(rating.text)
            total += float(rating.text)
            score = float((rating.text))
            score_1 = ("%.1f" % score)
            print(score_1)
            score_array.append(score_1)

    print(total)
    print("%.1f" % (total/4))

    return score_array

#google_scrape("lemeridien")
