import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pymysql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    conn = pymysql.connect( host='127.0.0.1',
                        user='an',
                        password='0000',
                        db='data',
                        charset='utf8'
                        )
    curs = conn.cursor()
    sql = "select * from rest;"
    curs.execute(sql)
    rows=curs.fetchall()
    rows = sorted(rows, key = lambda x:float(x[3]),reverse=True)
    return render_template('index.html', rows=rows)



@app.route('/post',methods =['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = str(request.form['name'])
        email = str(request.form['email'])
        phone = str(request.form['phone'])
        message = str(request.form['message'])
        conn = pymysql.connect( host='127.0.0.1',
                        user='an',
                        password='0000',
                        db='data',
                        charset='utf8'
                        )
        curs = conn.cursor()
        sql = "insert into reserv(name, email, phone, message) values(%s,%s,%s,%s)"
        curs.execute(sql, (name ,email, phone, message))
        conn.commit()
        
    return str(curs.rowcount) + "개가 전송 되었습니다."



if __name__ == '__main__':
    # https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.run
    # https://snacky.tistory.com/9
    app.run(host='0.0.0.0',debug=True)
