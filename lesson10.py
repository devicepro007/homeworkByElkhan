import mysql.connector as sql

conn = sql.connect(
    host="localhost",
    user="user",
    password="password",
    database="pylesson"
)

curs = conn.cursor()

print(conn)
print(curs)

# curs.execute("DELETE FROM table1")
# conn.commit()

for i in range(10):
    curs.execute(f"INSERT INTO `table1` (column1, column2) VALUES ('Hello', 'World');")
    conn.commit()

curs.execute("SELECT * FROM `table1`")
rows = curs.fetchall()

for row in rows:
    print(row)

conn.close()