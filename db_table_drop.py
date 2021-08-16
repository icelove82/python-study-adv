import db_connect as dbc

# 1. Get db
db = dbc.do_db_connect().cursor()

# 2. Make sql
sql = "DROP TABLE IF EXISTS test"

# 3. Select
db.execute(sql)
