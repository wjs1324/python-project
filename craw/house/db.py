import time
import threading
import schedule
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import pymysql
import emoji
import re

conn = pymysql.connect( host='localhost',
                        user='root',
                        password='0000',
                        db='data',
                        charset='utf8'
                        )
curs = conn.cursor()

print("20분 단위로 크롤링 프로그램을 실행합니다...(대기중)")


typelist = ['주택', '펜션', '아파트', '레지던스', '개인실', '호텔', '기타','호스텔','게스트','저택','하우스', '집','다인실','객실','로프트','캠핑카']

#------------------------------------------------------------------------------------

def deleteTable():
    curs.execute('DELETE FROM house2')
    conn.commit()


def craw(input_area):
    try:
        for jj in range(0,80,20):
            
            if input_area=='여수':
                area =  '여수' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/여수시--전라남도--대한민국/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJr6uLHx-UbTURi26I5drZAok&federated_search_session_id=99857d99-a7ea-4574-bfc6-94dc19b8fa40&pagination_search=true&items_offset='+str(jj)+'&section_offset=3')
            elif input_area =='거제도':
                area =  '거제도' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%EA%B1%B0%EC%A0%9C%EB%8F%84--%EA%B1%B0%EC%A0%9C%EC%8B%9C--%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84--%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=search_query&place_id=ChIJ3R7MqG_NbjURkgnJ-vfXysA&federated_search_session_id=d79d8995-4328-4a76-b304-52a0a8a67875&pagination_search=true&items_offset='+str(jj)+'&section_offset=3')
            elif input_area =='제주도':
                area =  '제주도' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%EC%A0%9C%EC%A3%BC%EB%8F%84/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=search_query&place_id=ChIJRUDITFTjDDURMb8emNI2vGY&federated_search_session_id=e9d1113c-6288-4ecf-b20c-8dd3056055ad&pagination_search=true&items_offset='+str(jj)+'&section_offset=3')
            elif input_area =='속초':
                area =  '속초' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%EC%86%8D%EC%B4%88%EC%8B%9C--%EA%B0%95%EC%9B%90%EB%8F%84--%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJsT1we_S82F8RyD8ltFjA9Ho&federated_search_session_id=2332a722-dde6-4941-b74c-925769416a88&pagination_search=true&items_offset='+str(jj)+'+&section_offset=4')
            elif input_area =='포항':
                area =  '포항' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%ED%8F%AC%ED%95%AD%EC%8B%9C--%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84--%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJM8KTwLr9ZjURftSE6Hw24sg&federated_search_session_id=3c6bb8d1-5d93-4493-831d-b8b665cf16c1&pagination_search=true&items_offset='+str(jj)+'&section_offset=4')
            elif input_area =='강릉':
                area =  '강릉' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%EA%B0%95%EB%A6%89%EC%8B%9C--%EA%B0%95%EC%9B%90%EB%8F%84--%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&adults=1&source=structured_search_input_header&search_type=search_query&place_id=ChIJWw9PleHlYTURRh09nFHGt4A&federated_search_session_id=d9500f8f-89a5-42d3-971c-36bd5c828fe5&pagination_search=true&items_offset='+str(jj)+'&section_offset=4')
            elif input_area =='부산':
                area =  '부산' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/부산광역시/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJNc0j6G3raDURpwhxJHTL2DU&federated_search_session_id=09299d74-471f-4552-8889-caa0595499aa&pagination_search=true&items_offset='+str(jj)+'&section_offset=3')
            elif input_area =='가평':
                area =  '가평' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%EA%B0%80%ED%8F%89%EA%B5%B0--%EA%B2%BD%EA%B8%B0%EB%8F%84--%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=search_query&place_id=ChIJp3mNK-ooYzURCQHqedpn6CU&federated_search_session_id=8c696d65-f453-47ab-8337-c5802025917a&pagination_search=true&items_offset='+str(jj)+'&section_offset=4')
            elif input_area =='경주':
                area =  '경주' #input("지역을 입력 해 주세요 : ")
                resp = requests.get('https://www.airbnb.co.kr/s/%EA%B2%BD%EC%A3%BC%EC%8B%9C--%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84--%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-08-07&checkout=2021-08-08&source=structured_search_input_header&search_type=search_query&place_id=ChIJHQMN-EZOZjURCcjQz-6WFTc&federated_search_session_id=87e9e120-c859-45bf-9468-04ac23a34ed1&pagination_search=true&items_offset='+str(jj)+'&section_offset=4')
                
            soup = BeautifulSoup(resp.text, 'html.parser')
    # 크롤링 태그 
            star = soup.select('._12oal24 ._h34mg6')
            comment = soup.select('._a7a5sx')
            name = soup.select('._12oal24 ._r6zroz ._5kaapu ._1whrsux9')
            type_ = soup.select('._1olmjjs6')
            cnt=0
            s=[] # star
            n=[] # name
            r=[] # review
            t = [] # type
            l = [] # area

# 별 점  및 후기 
            for i in star:
                a = i.text
                try:
                    b = a.split(" ")
                    c = b[1].split("개")
                    r.append(int(c[0]))
                    s.append(float(a[:4]))
                except:
                    s.append(0)
                    r.append(0)
    

    # 지역 
            for i in range(20):
                l.append(area)


# 이름 
            for i in name:
                a=i.text
                n.append(a[:30] + '~~')

# 숙소 유형 리스트
            for i in type_:    
                a= i.text
                print(a)
                for j in range(len(typelist)):
                    if typelist[j] in a :
                        t.append(typelist[j])
                        break
            print("별점 갯 수 ",len(s))
            print("이름 갯 수 ",len(n))
            print("리뷰 갯 수 ",len(r))
            print("타입 갯 수 ",len(t))
            print("지역 갯 수 ",len(l))
            print("샘플 데이터:")
            print(l[0] ,s[0], r[0], n[0], t[0])
            ok = 'y'  #input("갯 수와 데이터가 옳습니까? (y or n) : ")
            print(type_)
            alpha = []
            for i in range(len(n)):
                alpha.append(emoji.get_emoji_regexp().sub(u'', n[i]))
                
            if ok=='y':
                sql = "insert into house2(area, star, comment, name, kind) values(%s,%s,%s,%s,%s)"
                for i in range(len(l)):
                    curs.execute(sql, (l[i] ,s[i], r[i], re.sub('[^A-Za-z0-9가-힣]', '', alpha[i]), t[i]))
                    conn.commit()
                    print(curs.rowcount,"개가 입력 되었습니다. ")
                    
            else:
                pass
            s.clear() # star
            n.clear() # name
            r.clear() # review
            t.clear() # type
            l.clear() # area
    except:
        print("인덱스 오류")




t=20


schedule.every(t).minutes.do(deleteTable)
schedule.every(t).minutes.do(craw,'여수')
schedule.every(t).minutes.do(craw,'부산')
schedule.every(t).minutes.do(craw,'가평')
schedule.every(t).minutes.do(craw,'포항')
schedule.every(t).minutes.do(craw,'경주')
schedule.every(t).minutes.do(craw,'거제도')
schedule.every(t).minutes.do(craw,'제주도')
schedule.every(t).minutes.do(craw,'강릉')
schedule.every(t).minutes.do(craw,'속초')




while True:
    schedule.run_pending()
    #time.sleep(0.2)
