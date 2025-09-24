import pymysql

# 1.连接MySQL
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='20021203', charset='utf8',db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令
cursor.execute("insert into admin(username,password,mobile) values ('ashgalaxy','123123','12312312312')")
conn.commit()

# 3.关闭连接
cursor.close()
conn.close()