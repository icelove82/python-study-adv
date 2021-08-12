import db_connect

# 1. Connect
db = db_connect.do_db_connect().cursor()

# 2. Create db
try:
    db.execute('CREATE DATABASE study')
except Exception as err:
    print(err)

# 3. Show db list
db.execute('SHOW DATABASES')
print('***** DB List *****')
for item in db:
    print(item)

# 4. Create table
try:
    db.execute("""
        create table student
        (
            ID   int auto_increment
                primary key,
            NAME varchar(100) charset utf8 null,
            AGE  int                       null
        )
    """)
except Exception as err:
    print(err)

# 5. Show tables
db.execute('SHOW TABLES')
print('***** Table List *****')
for item in db:
    print(item)