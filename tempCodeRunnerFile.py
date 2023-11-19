cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emotions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        joy REAL,
        anger REAL,
        love REAL,
        sadness REAL,
        fear REAL,
        surprise REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')