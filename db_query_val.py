import db_connect as dbc

# 1. Get db
db = dbc.do_db_connect().cursor()

# 2. Make sql
sql = "SELECT * FROM customers WHERE ADDRESS = %s"
adr = ("Valley 345", )

# 3. Select
db.execute(sql, adr)

# 4. Result
result = db.fetchall()
for data in result:
    print(data)