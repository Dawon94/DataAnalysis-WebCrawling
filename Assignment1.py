import requests
from bs4 import BeautifulSoup

r = requests.get("http://lambutan.dothome.co.kr")
c = r.content

soup = BeautifulSoup(c,"html.parser")
all = soup.find("tbody")
all2 = all.find_all("tr",{"class":""})

for item in all2:
    aboutExam = item.find("td",{"class":"aboutexam hidden-lg hidden-md hidden-sm hidden-xs"}).text
    method = item.find("td",{"class":"method hidden-lg hidden-md hidden-sm hidden-xs"}).text

    print("AboutExam:" + aboutExam + "\n Method:"+ method)
