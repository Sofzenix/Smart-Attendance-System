import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import Config
from database.db import get_db_connection

def send_absentee_emails():
    conn = get_db_connection()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Get all active employees
    employees = conn.execute("SELECT id, name, email FROM users WHERE role='employee'").fetchall()
    
    # Get all users who marked attendance today
    present_user_ids = [row['user_id'] for row in conn.execute("SELECT DISTINCT user_id FROM attendance WHERE date=?", (today,)).fetchall()]
    
    absent_users = [emp for emp in employees if emp['id'] not in present_user_ids]
    
    if not absent_users:
        print("No absentees today.")
        conn.close()
        return

    # Check if SMTP credentials exist
    if not Config.MAIL_USERNAME or not Config.MAIL_PASSWORD:
        print("Mail config not set in environment. Skipping email dispatch for:")
        for u in absent_users:
            print(f" - {u['name']} ({u['email']})")
        conn.close()
        return

    try:
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        server.starttls()
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")
        conn.close()
        return

    for user in absent_users:
        msg = MIMEMultipart()
        msg['From'] = Config.MAIL_DEFAULT_SENDER
        msg['To'] = user['email']
        msg['Subject'] = "SmartFace: Action Required - Attendance Not Marked"
        
        body = f"""Dear {user['name']},

Our system detected that you were absent today ({today}). 
Please update your attendance or inform HR if required.

Best regards,
SmartFace Admin
"""
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server.send_message(msg)
            print(f"Sent email to {user['email']}")
        except Exception as e:
            print(f"Failed to send email to {user['email']}: {e}")

    server.quit()
    conn.close()
    print("Absentee detection complete.")

if __name__ == "__main__":
    send_absentee_emails()
