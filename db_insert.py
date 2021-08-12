import db_connect as dbc

# 1. Get cursor
db = dbc.do_db_connect().cursor()

# 2. Make sql
sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('John', 'Highway 21')

# 3. Insert
db.execute(sql, val)
dbc.do_db_connect().commit()

# 4. Print result
print(db.rowcount, ' recode inserted')
print('The insert row ID is :', db.lastrowid)

# 5. Insert many
vals = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

db.executemany(sql, vals)
dbc.do_db_connect().commit()
print(db.rowcount, ' recode inserted')