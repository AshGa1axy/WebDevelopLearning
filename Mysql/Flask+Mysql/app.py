import pymysql
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/add/user',methods=['POST','GET'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')

    username = request.form.get("username")
    password = request.form.get("password")
    mobile = request.form.get("mobile")

    # 1.连接MySQL
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='20021203', charset='utf8', db='mysqllearning')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2.发送指令
    sql = "insert into tb1(username,password,mobile) values (%s,%s,%s)"
    cursor.execute(sql,[username,password,mobile])
    conn.commit()

    # 3.关闭连接
    cursor.close()
    conn.close()

    return "添加成功"

if __name__ == '__main__':
    app.run()