import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_restoran',
)

try:
    with connection.cursor () as cursor:
        sql = "SELECT kd_user, nama, no_hp, username, password 'desc' FROM tb_user"
        try:
            cursor.execute (sql)
            result = cursor.fetchall ()
            print ("Kode User\tNama\tNo HP\tUsername\tPassword")
            print ("----------------------------------------------------------")
            for row in result:
                print (str (row[0]) + "\t" + row[1] + "\t" + row[2]+ "\t" + row[3]+ "\t" + row[4])
        except:
            print ("Oops! Something wrong")
    connection.commit ()
finally:
    connection.close ()