import sqlite3 as sq

conn = sq.connect('data.db')
cursor = conn.cursor()

borrar = '''
DROP TABLE DATA
'''
cursor.execute(borrar)

table = ''' CREATE TABLE DATA (
    Hora DATETIME NOT NULL UNIQUE,
    Capacidad INT,
    Voltaje FLOAT,
    Entrada INT,
    Salida INT
    )
    '''

cursor.execute(table)

cursor.execute('INSERT INTO DATA VALUES ("2022-04-03 10:10:21",45,46,47,36)')

conn.close()