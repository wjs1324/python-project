import requests
from bs4 import BeautifulSoup


resp = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B0%95%EB%A6%89+%EB%A7%9B%EC%A7%91&oquery=%ED%95%B4%EC%9A%B4%EB%8C%80+%EB%A7%9B%EC%A7%91&tqi=hLHBllp0YihssjHzoENssssss3N-506448')
soup=BeautifulSoup(resp.text,'html.parser')

blog =soup.select('span._2FqTn')

#print(blog)


a=[]
li1=[]
result_li1=[]
li2=[]
result_li2=[]
li3=[]
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
