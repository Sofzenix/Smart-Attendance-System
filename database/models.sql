CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_code TEXT UNIQUE,
    name TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    department TEXT,
    role TEXT,
    password TEXT,
    face_embedding BLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    date TEXT,
    check_in_time TEXT,
    status TEXT,
    FOREIGN KEY(employee_id) REFERENCES employees(id)
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);
