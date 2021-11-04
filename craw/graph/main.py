import recommand
import prefer
import schedule
import time
import type_

t=20


print("20분 간격으로 표를 제작 합니다...(로딩중)")
schedule.every(t).minutes.do(recommand.avg_graph,'여수')
schedule.every(t).minutes.do(recommand.avg_graph,'부산')
schedule.every(t).minutes.do(recommand.avg_graph,'거제도')
schedule.every(t).minutes.do(recommand.avg_graph,'강릉')
schedule.every(t).minutes.do(recommand.avg_graph,'제주도')
schedule.every(t).minutes.do(recommand.avg_graph,'가평')
schedule.every(t).minutes.do(recommand.avg_graph,'경주')
schedule.every(t).minutes.do(recommand.avg_graph,'속초')
schedule.every(t).minutes.do(recommand.avg_graph,'포항')
schedule.every(t).minutes.do(prefer.avg_graph)
schedule.every(t).minutes.do(type_.create_html)
while True:
    schedule.run_pending()
