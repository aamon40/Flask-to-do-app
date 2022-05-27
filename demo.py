import psycopg2

connection = psycopg2.connect('dbname=postgres user=postgres password=root host=localhost')

cursor = connection.cursor()

cursor.execute('DROP  TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')
# %s turns the string into a template that we can the inject data into and then we pass in  as the second argument to the execute method, the order in which we want to replace the templates inside a tuple
cursor.execute('INSERT INTO table2 ( id, completed) VALUES ( %s, %s);', (1, True))


# A different method of string composition; we use named variables and instead of a tuple we pass in a dictionary that includes those named variables. To make the code cleaner, we assign the template string and the dictionary to named variables
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 2,
    'completed': False
}

cursor.execute(SQL, data)

cursor.execute('INSERT INTO table2 ( id, completed) VALUES ( %s, %s);', (3, True))

cursor.execute('SELECT * FROM table2;')

result = cursor.fetchmany(2)
print('fetchmany', result)

result2 = cursor.fetchone()
print('fetchone', result2)

connection.commit()

connection.close()
cursor.close()

