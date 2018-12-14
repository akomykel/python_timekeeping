import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", db="testgodb")

myCursor = conn.cursor()

myCursor.execute("SELECT * FROM players;")

print(myCursor.fetchall())

conn.commit()
conn.close()

