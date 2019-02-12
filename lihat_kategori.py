import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_restoran',
)

try:
    with connection.cursor () as cursor:
        sql = "SELECT kd_kategori, kategori, 'desc' FROM tb_kategori"
        try:
            cursor.execute (sql)
            result = cursor.fetchall ()

            print ("Kode Kategori\t\t\tKategori")
            print ("----------------------------------------------------------")
            for row in result:
                print (str (row[0]) + "\t\t\t\t" + row[1] )

        except:
            print ("Oops! Something wrong")

    connection.commit ()
finally:
    connection.close ()