import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_restoran',
)

kd_user = input ("Kd Kategori : ")
nama = input ("Nama : ")
no_hp = input ("No HP : ")
username = input ("Username : ")
password = input ("Password : ")

try:
    with connection.cursor () as cursor:
        sql = "INSERT INTO tb_user VALUES (%s, %s, %s, %s, %s)"

        try:
            cursor.execute (sql, (kd_user, nama, no_hp, username, password))
            print ("Berhasil")
        except:
            print ("Gagal")

    connection.commit ()
finally:
    connection.close ()