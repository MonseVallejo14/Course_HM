import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
r = requests.get(url)
text = r.text
soup = BeautifulSoup(text, "html.parser")

questions = soup.select(".s-post-summary")
print(questions[0]["data-post-id"])
for question in questions:
    title = question.select_one(".s-link").get_text()
    user = question.select_one(".s-user-card--link").get_text()
    # print(f"{user.strip()} - Title: \n{title.strip()}")
