import pymysql


def test_connect(host, port, user, pwd, db):
    db = pymysql.connect(host=host, port=port, user=user, password=pwd, database=db)
    cursor = db.cursor()

    cursor.execute("select * from sys_dict where second_dict_key != ''")
    data = cursor.fetchall()

    print(data)
    db.close()


if __name__ == '__main__':
    test_connect('10.8.160.110', 3306, 'root', 'mysql@123456', 'narwal_production_auth')