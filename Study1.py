import requests
from bs4 import BeautifulSoup


#requests 라이브러리를 이용해 홈페이지에 접속 후 컨텐츠 가져오기
r = requests.get("http://lambutan.dothome.co.kr")
c = r.content

#위의 방법 처럼 가져오면 가독성이 떨어짐
#Beautifulsoup의 html.parser 메소드로 보기 쉽게 정렬하기
soup = BeautifulSoup(c,"html.parser")
all = soup.find("tbody")
all2 = all.find_all("tr",{"class":""})

for item in all2:
    professor = item.find("td",{"class":"professor"}).text
    lectureName = item.find("td",{"class":"lecture"}).text
    orther = item.find("td",{"class":"orther"}).text
    grade = item.find("td",{"class":"grade"}).text
    evaluation = item.find("td",{"class":"evaluation"}).text
    print(professor + "/" + lectureName + "/" + orther + "/" + evaluation)



