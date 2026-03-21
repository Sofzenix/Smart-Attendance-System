import sqlite3
import os
from config import Config

def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE_URI)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    conn = get_db_connection()
    conn.executescript(schema)

    # Insert a default admin if not exists
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE role = 'admin'")
    if not cur.fetchone():
        from werkzeug.security import generate_password_hash
        default_admin_pw = generate_password_hash("admin123")
        cur.execute('''
            INSERT INTO users (employee_id, name, email, phone, department, password_hash, role, face_registered)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ('ADMIN001', 'Super Admin', 'admin@sofzenix.com', '0000000000', 'Management', default_admin_pw, 'admin', 0))
    
    conn.commit()
    conn.close()
