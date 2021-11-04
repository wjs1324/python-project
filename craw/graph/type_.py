import pymysql
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

conn = pymysql.connect( host='localhost',
                        user='root',
                        password='0000',
                        db='data',
                        charset='utf8'
                        )
curs = conn.cursor()
sql = "select * from house2"
curs.execute(sql)
rows=curs.fetchall()


def create_html():



    
    print(rows[0][5])
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0
    cnt6 = 0
    cnt7 = 0
    cnt8 = 0

    for i in range(len(rows)):
        if rows[i][5]=='호텔':
            cnt1 +=1
        elif rows[i][5]=='펜션':
            cnt2 +=1
        elif rows[i][5]=='주택':
            cnt3 +=1
        elif rows[i][5]=='아파트':
            cnt4 +=1
        elif rows[i][5]=='레지던스':
            cnt5 +=1
        elif rows[i][5]=='게스트':
            cnt6 +=1
        elif rows[i][5]=='개인실':
            cnt7 +=1
        elif rows[i][5]=='호스텔':
            cnt8 +=1
        print(rows[i][5])



    data = {'호텔':[cnt1],
        '펜션':[cnt2],
        '주택':[cnt3],
        '아파트':[cnt4],
        '레지던스':[cnt5],
        '게스트':[cnt6],
        '개인실':[cnt7],
        '호스텔':[cnt8]
}


    df = pd.DataFrame(data,index=['빈도'])
    df

    df.to_html("test.html",encoding='utf-8')
    print("타입 생성이 완료 되었습니다.")


