import sqlite3

conn = sqlite3.connect("fila.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Tabela 'usuarios' criada com sucesso (ou já existia).")
