import sqlite3

def conectar_banco():
    conn = sqlite3.connect("fila.db")
    cursor = conn.cursor()
    
    # Criar a tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fila (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    return conn, cursor

def adicionar_na_fila(nome):
    conn, cursor = conectar_banco()
    cursor.execute("INSERT INTO fila (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def chamar_proximo():
    conn, cursor = conectar_banco()
    cursor.execute("SELECT id, nome FROM fila ORDER BY id ASC LIMIT 1")
    proximo = cursor.fetchone()
    
    if proximo:
        cursor.execute("DELETE FROM fila WHERE id = ?", (proximo[0],))
        conn.commit()
        conn.close()
        return proximo[1]
    
    conn.close()
    return None
def listar_fila():
    conn, cursor = conectar_banco()
    cursor.execute("SELECT * FROM fila ORDER BY id ASC")
    pessoas = cursor.fetchall()
    conn.close()
    
    return [{"id": p[0], "nome": p[1]} for p in pessoas]
