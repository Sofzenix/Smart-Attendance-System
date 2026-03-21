import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from database.db import get_db_connection, init_db
from utils.face_utils import register_face, recognize_face

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database dynamically
if not os.path.exists(Config.DATABASE_URI):
    os.makedirs(os.path.dirname(Config.DATABASE_URI), exist_ok=True)
    init_db()

@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("admin_dashboard") if session.get("role") == "admin" else url_for("employee_dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["role"] = user["role"]
            session["name"] = user["name"]
            
            return redirect(url_for("admin_dashboard") if user["role"] == "admin" else url_for("employee_dashboard"))
        else:
            flash("Invalid email or password", "danger")
            
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        emp_id = request.form.get("employee_id")
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        dept = request.form.get("department")
        password = request.form.get("password")
        
        hashed_pw = generate_password_hash(password)
        conn = get_db_connection()
        
        try:
            conn.execute('''
                INSERT INTO users (employee_id, name, email, phone, department, password_hash, role)
                VALUES (?, ?, ?, ?, ?, ?, 'employee')
            ''', (emp_id, name, email, phone, dept, hashed_pw))
            conn.commit()
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Employee ID or Email already exists.", "danger")
        finally:
            conn.close()
            
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# --- ADMIN ROUTES ---
@app.route("/admin")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect(url_for("login"))
        
    conn = get_db_connection()
    total_emp = conn.execute("SELECT COUNT(*) FROM users WHERE role='employee'").fetchone()[0]
    
    today = datetime.now().strftime("%Y-%m-%d")
    present_today = conn.execute("SELECT COUNT(DISTINCT user_id) FROM attendance WHERE date = ?", (today,)).fetchone()[0]
    
    recent_attendance = conn.execute('''
        SELECT attendance.time, attendance.status, users.name, users.employee_id
        FROM attendance
        JOIN users ON attendance.user_id = users.id
        WHERE attendance.date = ?
        ORDER BY attendance.time DESC LIMIT 10
    ''', (today,)).fetchall()
    
    conn.close()
    return render_template("admin_dashboard.html", 
                           total_emp=total_emp, 
                           present_today=present_today, 
                           absent_today=total_emp - present_today,
                           recent_attendance=recent_attendance)


# --- EMPLOYEE ROUTES ---
@app.route("/employee")
def employee_dashboard():
    if session.get("role") != "employee":
        return redirect(url_for("login"))
    
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],)).fetchone()
    history = conn.execute("SELECT * FROM attendance WHERE user_id = ? ORDER BY date DESC, time DESC LIMIT 10", (session["user_id"],)).fetchall()
    conn.close()
    
    return render_template("employee_dashboard.html", user=user, history=history)


# --- FACE SCANNER ROUTE ---
@app.route("/scanner")
def scanner():
    # Allow scanner access either to admins (kiosk mode) or let it be an open kiosk
    # For a real attendance kiosk, it should be logged in as admin or dedicated user.
    if session.get("role") != "admin":
        return redirect(url_for("login"))
    return render_template("scanner.html")


# --- API ENDPOINTS ---
@app.route("/api/register_face", methods=["POST"])
def api_register_face():
    if "user_id" not in session:
        return jsonify({"success": False, "msg": "Unauthorized"}), 401
        
    data = request.json
    base64_img = data.get("image")
    
    success = register_face(session["user_id"], base64_img)
    if not success:
        return jsonify({"success": False, "msg": "No face detected. Please try again."}), 400
    
    conn = get_db_connection()
    conn.execute("UPDATE users SET face_registered = 1 WHERE id = ?", (session["user_id"],))
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "msg": "Face registered successfully! You can now mark attendance."})


@app.route("/api/recognize_face", methods=["POST"])
def api_recognize_face():
    data = request.json
    base64_img = data.get("image")
    
    user_id = recognize_face(base64_img)
    
    if user_id:
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        conn = get_db_connection()
        existing = conn.execute("SELECT id FROM attendance WHERE user_id=? AND date=?", (user_id, date_str)).fetchone()
        
        user_info = conn.execute("SELECT name, employee_id FROM users WHERE id=?", (user_id,)).fetchone()
        
        if not existing:
            conn.execute("INSERT INTO attendance (user_id, date, time, status) VALUES (?, ?, ?, ?)",
                         (user_id, date_str, time_str, "Present"))
            conn.commit()
            
            conn.close()
            return jsonify({
                "success": True, 
                "msg": f"Attendance marked for {user_info['name']}", 
                "user": user_info['name'],
                "emp_id": user_info['employee_id']
            })
        else:
            conn.close()
            return jsonify({"success": True, "msg": f"{user_info['name']}, you have already marked attendance today."})
    
    return jsonify({"success": False, "msg": "Face not recognized. Please scan again."})

if __name__ == "__main__":
    app.run(debug=True)
