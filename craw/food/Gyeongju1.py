import pymysql

conn = pymysql.connect(
    user='root',
    passwd='0000',
    host='localhost',
    db='Data',
    charset='utf8'
)

curs = conn.cursor(pymysql.cursors.DictCursor)




import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup

area = input("지역을 입력 해 주세요 : ")

resp = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%A3%BC+%EB%A7%9B%EC%A7%91&oquery=%EA%B1%B0%EC%A0%9C%EB%8F%84+%EB%A7%9B%EC%A7%91&tqi=hLIo1sp0YihsstM6GA0ssssst80-437890')
soup=BeautifulSoup(resp.text,'html.parser')

name = soup.select('.OXiLu')
blog =soup.select('span._2FqTn')

print(name)
cnt=0

n=[]
a=[]
l=[]
li1=[]#별점
result_li1=[]
li2=[]#방문자리뷰
result_li2=[]
li3=[]#블로그리뷰
result_li3=[]

for i in blog:
    a.append(i.text)


for i in range(len(a)):
    if i==0 or i%3==0:
        li1.append(a[i])
    elif i==1 or i%3==1:
        li2.append(a[i])
    else:
        li3.append(a[i])

for i in li1:
    temp = i.replace("별점","")
    result_li1.append(temp)

for i in li2:
    temp = i.replace("방문자리뷰 ","")
    result_li2.append(temp)

for i in li3:
    temp = i.replace("블로그리뷰 ","")
    result_li3.append(temp)

print(result_li1)
print(result_li2)
print(result_li3)



for i in range(8):
    l.append(area)


# 이름
for i in name:
    a=i.text
    n.append(a)

print(n)



print("이름 갯 수 ",len(n))
print("지역 갯 수",len(l))
print("별점 갯 수", len(result_li1))
print("방문자 리뷰 갯 수 ",len(result_li2))
print("블로그 리뷰 갯 수 ",len(result_li3))
print("샘플 데이터:")




ok = input("갯 수와 데이터가 옳습니까? (y or n) : ")

if ok=='y':
    sql = "insert into rest(name, area, star, visitor, blog) values(%s,%s,%s,%s,%s)"
    for i in range(len(n)):
        curs.execute(sql, (n[i] ,l[i], result_li1[i], result_li2[i], result_li3[i]))
        conn.commit()
        print(curs.rowcount,"개가 입력 되었습니다. ")
else:
    pass
