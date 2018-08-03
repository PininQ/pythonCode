from datetime import date, datetime, timedelta
import pymysql.cursors
'''
连接本地的 MySQL 数据库，需先在数据库中创建 testDB 数据库，执行如下语句向 testDB 中插入一条记录
'''
# 连接配置信息
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'admin',
    'db': 'testDB',  # 先创建数据库testDB
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)

# 获取明天的时间
tomorrow = datetime.now().date() + timedelta(days=1)

# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(sql, ('qin', 'bin', tomorrow, 'M', date(1994, 11, 29)));
        print("-" * 50, "成功插入数据！", "-" * 50)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
