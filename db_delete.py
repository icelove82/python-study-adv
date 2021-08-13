import db_connect as dbc

# 1. Get db
db = dbc.do_db_connect().cursor()

# 2. Make sql
sql = "DELETE FROM customers WHERE ADDRESS = %s"
adr = ("Mountain 21", )

# 3. Select
db.execute(sql, adr)
dbc.do_db_connect().commit()

# 4. Result
print(db.rowcount, " recode(s) deleted")