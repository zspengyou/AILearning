from pymysql import Connection

con = Connection(
    host='localhost',
    port= 3306,
    user="root"
)

print(con.get_server_info())

cursor = con.cursor()
con.select_db("instance_2")
cursor.execute("select * from vof_cdms_subject_links__v limit 10")

result : tuple = cursor.fetchall()
for item in result:
    print(item)

con.close()