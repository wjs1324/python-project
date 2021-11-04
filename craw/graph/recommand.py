from matplotlib import pyplot as plt
import numpy
import pymysql
from matplotlib import rc




def house_area(input_area):


    conn = pymysql.connect( host='localhost',
                        user='root',
                        password='0000',
                        db='data',
                        charset='utf8'
                        )
    curs = conn.cursor()


    if input_area == '여수':
        sql = "select * from house2 where area=\'여수\'"
    elif input_area == '제주도':
        sql = "select * from house2 where area=\'제주도\'"
    elif input_area == '거제도':
        sql = "select * from house2 where area=\'거제도\'"
    elif input_area == '포항':
        sql = "select * from house2 where area=\'포항\'"
    elif input_area == '부산':
        sql = "select * from house2 where area=\'부산\'"
    elif input_area == '강릉':
        sql = "select * from house2 where area=\'강릉\'"
    elif input_area == '속초':
        sql = "select * from house2 where area=\'속초\'"
    elif input_area == '가평':
        sql = "select * from house2 where area=\'가평\'"
    elif input_area == '경주':
        sql = "select * from house2 where area=\'경주\'"
    curs.execute(sql)
    rows=curs.fetchall()
    area = []
    for i in rows:
        area.append(i)
    area= sorted(area, key = lambda x:float(x[3]),reverse=True)
    print(area)
    return area



def avg_graph(input_data):

    rc('font', family='AppleGothic')

    plt.rcParams['axes.unicode_minus'] = False
    
    a = house_area(input_data)
    
    fir = a[0]
    sec = a[1]
    thi = a[2]
    fou = a[3]
    fiv = a[4]

    #print(fir[4][:7])
    #print(sec[4][:7])
    #print(thi[4][:7])
    #print(fou[4][:7])
    #print(fiv[4][:7])

    x_values = [fiv[4][:7], fou[4][:7], thi[4][:7], sec[4][:7], fir[4][:7]]	# x축 지점의 값들
    y_values = [float(fiv[3]),float(fou[3]),float(thi[3]),float(sec[3]),float(fir[3])]         # 리뷰수 

    x = numpy.arange(len(x_values))
    plt.bar(x_values, y_values, color='#339933')	# line 그래프를 그립니다

    plt.xlabel('지역')
    plt.ylabel('후기 수')
    plt.title(input_data+"지역의 후기 수 TOP")

    plt.savefig(input_data+'_review.png')
    plt.close()


    # ----------------------------------------------

    x_values = [fiv[4][:7], fou[4][:7], thi[4][:7], sec[4][:7], fir[4][:7]]	# x축 지점의 값들
    y_values = [float(fiv[2]),float(fou[2]),float(thi[2]),float(sec[2]),float(fir[2])]         #

    x = numpy.arange(len(x_values))
    plt.bar(x_values, y_values, color='#0099ff')	# line 그래프를 그립니다

    plt.xlabel('지역')
    plt.ylabel('평점')
    plt.title(input_data+"지역의 평점 TOP")

    plt.savefig(input_data+'_star.png')
    plt.close()

    del fir
    del sec
    del thi
    del fou
    del fiv

