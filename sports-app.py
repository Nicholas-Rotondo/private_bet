from bs4 import BeautifulSoup
import requests
import time

# sports_decision = input("Pick a sport: ")
# live_decision = input("Would you like to view live games or finished games: ")

# Different website to scrape
# r = requests.get("https://www.scoreboard.com/en/")

# oldtime = time.perf_counter()
#
# elapsed_time = time.time - old_time

# def get_time(oldtime):
#     current_time = time.time()

def get_scores():
    r1 = requests.get("https://www.scorespro.com/")

    soup = BeautifulSoup(r1.content, "html.parser")

    data = soup.find("div", id="wholescoreline")
    for link in data:
        try:
            display = link.contents[0].text
            print(display)
        except:
            pass

get_scores()
