from flask import Flask, render_template, request, redirect, session
import sqlite3

from face_module.register_face import capture_face
from face_module.recognize_face import recognize_faces

# ✅ Create app FIRST
app = Flask(__name__)

# ✅ Add secret key AFTER app creation
app.secret_key = "secret123"


# Database connection
def get_connection():
    conn = sqlite3.connect("database/employees.db")
    conn.row_factory = sqlite3.Row
    return conn


    # ✅ ADD HERE
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        department TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

# ✅ CALL IT HERE (IMPORTANT)
init_db()

# ✅ LOGIN FIRST
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["user"] = username   # ✅ ADD THIS
            return redirect("/admin")
        else:
            return "Invalid Login"

    return render_template("login.html")



# ✅ HOME ROUTE
@app.route("/")
def home():
    return redirect("/login")


# ---------------- ADMIN DASHBOARD ----------------
@app.route("/admin")
def admin_dashboard():

    # ✅ PROTECTION
    if "user" not in session:
        return redirect("/login")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM employees")
    total = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM attendance WHERE date = DATE('now')")
    present = cur.fetchone()[0]

    absent = total - present

    conn.close()

    return render_template(
        "admin_dashboard.html",
        total=total,
        present=present,
        absent=absent
    )


# ---------------- ADD EMPLOYEE ----------------
@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO employees (name, email, department) VALUES (?, ?, ?)",
            (name, email, department)
        )

        conn.commit()
        conn.close()

        return redirect("/admin")

    return render_template("add_employee.html")

@app.route("/attendance")
def attendance():

    # ✅ PROTECTION (important)
    if "user" not in session:
        return redirect("/login")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT employees.name, attendance.date
    FROM attendance
    JOIN employees ON employees.id = attendance.employee_id
    """)

    data = cur.fetchall()
    conn.close()

    return render_template("attendance.html", records=data)



# ---------------- VIEW EMPLOYEES ----------------
@app.route("/employees")
def employees():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()

    conn.close()

    return render_template("employees.html", employees=data)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")



# ---------------- RUN APP ----------------
init_db()

if __name__ == "__main__":
    app.run(debug=True)


