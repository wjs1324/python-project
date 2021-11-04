from matplotlib import pyplot as plt
import numpy
import pymysql
from matplotlib import rc


conn = pymysql.connect( host='localhost',
                        user='root',
                        password='0000',
                        db='data',
                        charset='utf8'
                        )
curs = conn.cursor()



# 별점 평균 구하기
def avg_star(input_area):

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
    star = []
    for i in rows:
#        if float(i[2]) == 0:
#           pass
#      else:
            star.append(float(i[2]))     # 별점 다 가져오기

    print(input_area,"의 평균 평점 :", round(sum(star)/len(star),3))
    return round(sum(star)/len(star),3)



# 리뷰 평균 구하기 
def avg_review(input_area):
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
    review = []
    for i in rows:
#        if float(i[2]) == 0:
#           pass
#      else:
            review.append(float(i[3]))

    print(input_area,"의 평균 평점 :", round(sum(review)/len(review),3))
    return round(sum(review)/len(review),3)


def avg_graph():

    rc('font', family='AppleGothic')

    plt.rcParams['axes.unicode_minus'] = False
    
    star_yeosu = avg_star('여수')
    star_jeju = avg_star('제주도')
    star_geoje = avg_star('거제도')
    star_pohang = avg_star('포항')
    star_pusan =avg_star('부산')
    star_gangreung =avg_star('강릉')
    star_gapyeong =avg_star('가평')
    star_gyeongju =avg_star('경주')
    star_sokcho =avg_star('속초')

    review_yeosu = avg_review('여수')
    review_jeju = avg_review('제주도')
    review_geoje = avg_review('거제도')
    review_pohang = avg_review('포항')
    review_pusan =avg_review('부산')
    review_gangreung =avg_review('강릉')
    review_gapyeong =avg_review('가평')
    review_gyeongju  =avg_review('경주')
    review_sokcho =avg_review('속초')

    x_values = ["여수", "제주", "거제", "포항", "부산","강릉", "가평","경주","속초"]	# x축 지점의 값들
    y_values = [star_yeosu, star_jeju, star_geoje, star_pohang, star_pusan, star_gangreung, star_gapyeong, star_gyeongju, star_sokcho]	# y축 지점의 값들
    y2_values = [review_yeosu, review_jeju, review_geoje , review_pohang , review_pusan, review_gangreung, review_gapyeong, review_gyeongju, review_sokcho ]	# y축 지점의 값들
    y3_values = [star_yeosu*review_yeosu/10,star_jeju*review_jeju/10,star_geoje*review_geoje/10,star_pohang*review_pohang/10,star_pusan*review_pusan/10,star_gangreung*review_gangreung/10,star_gapyeong*review_gapyeong/10,star_gyeongju*review_gyeongju/10,star_sokcho*review_sokcho/10]

    x = numpy.arange(len(x_values))
    plt.bar(x-0.0, y_values, label='별점', width=0.2, color='#dd0000')	# line 그래프를 그립니다
    plt.bar(x+0.2, y2_values, label='리뷰', width=0.2, color='#ddff00')
    plt.plot(x+0.1,y3_values,label='선호도', color='#000000')

    plt.xticks(x,x_values)
    plt.legend()
    plt.xlabel('지역')
    plt.ylabel('평균')
    plt.title('지역별 숙소 평균 평점 및 리뷰 수')

    plt.savefig('result.png')
    plt.close()
    #plt.show()	# 그래프를 화면에 보여줍니다


# 평균 별점
# 평균 리뷰
# 별정 * 리뷰 
