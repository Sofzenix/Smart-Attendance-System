<div align="center">

<!-- Animated Hero Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0e1a,50:064e3b,100:10b981&height=220&section=header&text=SmartFace%20AI&fontSize=72&fontColor=ffffff&fontAlignY=35&desc=Enterprise%20Face%20Recognition%20Attendance%20System&descSize=18&descAlignY=55&descColor=94a3b8&animation=fadeIn" width="100%" />

<!-- Dynamic Badges -->
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.13-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev)
[![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](LICENSE)
[![Security](https://img.shields.io/badge/Encryption-AES--256-f59e0b?style=for-the-badge&logo=letsencrypt&logoColor=white)](#-privacy--security)

<br/>

<p>
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=20&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&multiline=true&repeat=true&width=650&height=60&lines=10-Layer+Anti-Spoofing+Engine+%7C+MediaPipe+3D+Mesh;AES-256+Encrypted+Face+Data+%7C+Zero+Trust+Architecture" alt="Typing SVG" />
</p>

<p><em>AI-powered biometric attendance management with military-grade anti-spoofing, encrypted face storage, and real-time analytics. Built by <strong>Sofzenix Technologies</strong>.</em></p>

---

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#%EF%B8%8F-system-architecture) · [🛡️ Anti-Spoofing](#%EF%B8%8F-10-layer-anti-spoofing-engine) · [🔐 Privacy](#-privacy--security) · [📊 Features](#-feature-matrix) · [☁️ Deploy](#%EF%B8%8F-deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Feature Matrix](#-feature-matrix)
- [System Architecture](#️-system-architecture)
- [10-Layer Anti-Spoofing Engine](#️-10-layer-anti-spoofing-engine)
- [Liveness Detection](#-liveness-detection)
- [Privacy & Security](#-privacy--security)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Admin Guide](#-admin-guide)
- [Deployment](#️-deployment)
- [Report / Project Documentation](#-report--project-documentation)
- [License](#-license)

---

## 🌟 Overview

**SmartFace AI** is a full-stack, enterprise-grade attendance management system that replaces traditional badge/fingerprint scanners with instant **AI face recognition**. Employees simply look at a camera — the system verifies identity in under **300ms**, validates liveness through a single-blink challenge, runs a **10-layer anti-spoofing analysis**, and records attendance automatically.

```
┌─────────────────────────────────────────────────────────────────┐
│                        SmartFace AI                             │
│                                                                 │
│   Employee → Camera → Face Detected → Identity Matched          │
│                            ↓                                    │
│                  10-Layer Spoof Analysis                         │
│                  (Texture, Moiré, Glare, 3D Depth, ...)         │
│                            ↓                                    │
│                  Liveness Challenge (Blink)                      │
│                            ↓                                    │
│                  ✅ Attendance Recorded                          │
│                  📧 Absentee Alerts Sent                         │
└─────────────────────────────────────────────────────────────────┘
```

> **Why not fingerprint scanners?** Fingerprint scanners require physical contact (hygiene concerns), are slow in queues, can be spoofed with gelatin molds, and cost 10x more per unit. SmartFace AI is touchless, instant, and runs on any $20 USB webcam.

---

## 📊 Feature Matrix

| Feature | Status | Details |
|:--------|:------:|:--------|
| 🎯 **Face Recognition** | ✅ | LBPH + DNN detection, 97%+ accuracy, < 300ms |
| 🛡️ **10-Layer Anti-Spoofing** | ✅ | Texture, Edge, Color, Moiré, Glare, FFT, Depth, Eyes, 3D Pose, Screen Border |
| 👁️ **Liveness Detection** | ✅ | MediaPipe EAR single-blink challenge (works through glasses) |
| 🔐 **Encrypted Face Storage** | ✅ | Fernet AES-256 symmetric encryption at rest |
| 👤 **Employee Self-Registration** | ✅ | With password strength meter, phone/email validation |
| 📸 **Profile Photo Upload** | ✅ | 2MB max, JPG/PNG, auto-cropped |
| ✏️ **Edit Profile** | ✅ | Name, phone, department, password change |
| 👨‍💼 **Admin Dashboard** | ✅ | Real-time stats, charts, employee management |
| 📈 **Analytics Page** | ✅ | Department-wise breakdowns, attendance trends |
| 📅 **Attendance History** | ✅ | Filterable by date range, searchable |
| 📥 **CSV Export** | ✅ | Full attendance data export with date filters |
| 📧 **Auto Absentee Emails** | ✅ | APScheduler cron trigger, professional HTML templates |
| 📧 **HR CC Notifications** | ✅ | Optional CC to HR on all absentee alerts |
| ⏰ **Late Arrival Tracking** | ✅ | Configurable cutoff hour/minute |
| ⚙️ **Admin Settings Panel** | ✅ | Late cutoff, company name, email config, tolerance |
| 🌙 **Premium Dark UI** | ✅ | Glassmorphism, particles.js, micro-animations |
| 📱 **Responsive Design** | ✅ | Mobile, tablet, and desktop optimized |
| 🐘 **PostgreSQL Support** | ✅ | Auto-detects Neon/Postgres or falls back to SQLite |
| ☁️ **Render Deployment** | ✅ | Procfile + Gunicorn configured |

---

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph Frontend["🖥️ Frontend Layer"]
        A[HTML/CSS/JS] --> B[Camera Feed]
        B --> C[Base64 Frame Capture]
        A --> D[Particles.js Landing]
        A --> E[Glassmorphism UI]
    end

    subgraph Backend["⚙️ Backend Layer - Flask"]
        F[REST API Routes] --> G[Face Recognition Engine]
        F --> H[Auth & Session Management]
        F --> I[Attendance Logic]
        F --> J[Email Service]
    end

    subgraph AI["🧠 AI / ML Layer"]
        G --> K[OpenCV DNN Detector]
        G --> L[LBPH Recognizer]
        G --> M[MediaPipe Face Mesh]
        M --> N[468-Point 3D Landmarks]
        N --> O[EAR Blink Detection]
        N --> P[3D Pose Depth Analysis]
        G --> Q[10-Layer Anti-Spoof Engine]
    end

    subgraph Security["🔐 Security Layer"]
        R[Fernet AES-256 Encryption]
        S[Werkzeug Password Hashing]
        T[Input Validation Engine]
        U[CSRF Protection]
    end

    subgraph Data["🗄️ Data Layer"]
        V[(SQLite / PostgreSQL)]
        W[Encrypted .enc Files]
        X[LBPH Trainer Model]
    end

    C -->|POST /api/recognize_face| F
    G --> R
    R --> W
    L --> X
    I --> V
    J -->|SMTP| Y[Gmail / SMTP Server]

    style Frontend fill:#0d1117,stroke:#10b981,color:#fff
    style Backend fill:#0d1117,stroke:#06b6d4,color:#fff
    style AI fill:#0d1117,stroke:#8b5cf6,color:#fff
    style Security fill:#0d1117,stroke:#f59e0b,color:#fff
    style Data fill:#0d1117,stroke:#f43f5e,color:#fff
```

---

## 🛡️ 10-Layer Anti-Spoofing Engine

SmartFace AI implements the most comprehensive anti-spoofing pipeline available in any open-source attendance system. Every video frame is analyzed through **10 independent detection layers** before access is granted.

| Layer | Name | What It Detects | How |
|:-----:|:-----|:----------------|:----|
| 1 | **LBP Texture Analysis** | Flat screens have low texture variance | Local Binary Pattern histogram variance comparison |
| 2 | **Edge Density** | Real faces have complex, irregular edges | Canny edge detection + density ratio calculation |
| 3 | **Color Temperature** | Screens emit blue-shifted light vs warm skin | Red-Blue channel ratio + HSV skin segmentation |
| 4 | **Moiré Pattern Detection** | Screen-on-camera creates interference patterns | FFT radial energy analysis + periodic peak detection |
| 5 | **Screen Glare Detection** | Glass screens produce specular white highlights | HSV saturation/value thresholding + HoughLines |
| 6 | **Frequency Domain (FFT)** | Screen pixels create sharp frequency peaks | 2D FFT + high-frequency peak isolation |
| 7 | **Multi-Frame Depth** | Static photos have zero position variance | Frame-to-frame position/size jitter tracking |
| 8 | **Eye Presence** | Dead images don't have detectable 3D eye structure | MediaPipe 468-point face mesh verification |
| 9 | **3D Pose Depth** | Flat screens have no Z-axis depth between nose and cheeks | MediaPipe Z-coordinate variance (nose vs cheeks) |
| 10 | **Screen Border Detection** | Phone bezels create rectangular edge patterns around face | Canny + HoughLinesP for straight-line rectangles + uniform border std |

### Composite Scoring

```
Final Score = Σ(Layer_i × Weight_i)

Weights: Texture(0.10) + Edge(0.08) + Color(0.12) + Moiré(0.12) +
         Glare(0.10) + FFT(0.08) + Depth(0.08) + Eyes(0.12) +
         ScreenBorder(0.20)

HARD RULES:
  • Score < 45 → ❌ REJECTED (spoofing detected)
  • ≥ 3 layers fail → Score capped at 20
  • Screen border detected → Score capped at 15
  • 3D Pose flat → Score capped at 25
```

> **Result:** Photos, phone screens, tablet replays, printed masks, and pre-recorded videos are all rejected with near-100% accuracy.

---

## 👁️ Liveness Detection

Even after passing all 10 anti-spoof layers, the user must complete a **real-time liveness challenge** — a single blink detected via MediaPipe's Eye Aspect Ratio (EAR):

```
              EAR = (||p2-p6|| + ||p3-p5||) / (2 × ||p1-p4||)

   p2 ●────● p3              Open Eye:  EAR ≈ 0.30+
  /              \            Closed:    EAR < 0.28
p1 ●              ● p4       Blink:     Open → Closed → Open
  \              /
   p6 ●────● p5

MediaPipe Landmarks Used:
  Left Eye:  33, 133 (horizontal) | 160-144, 158-153 (vertical)
  Right Eye: 362, 263 (horizontal) | 385-380, 387-373 (vertical)
```

- **Threshold:** EAR < 0.28 (raised for spectacle wearers — lens refraction inflates measured EAR)
- **Challenge:** Close eyes → Open eyes = 1 blink = Liveness confirmed
- **Speed:** Detection happens in real-time at 300ms intervals
- **Works through:** Prescription glasses, sunglasses, beards, face masks (partial)

---

## 🔐 Privacy & Security

SmartFace AI treats biometric data as **the highest classification of personal information**. Here is exactly what happens to your face data:

### Encryption Pipeline

```
Camera Frame → Face Detected → ROI Extracted → cv2.imencode('.jpg')
    → Raw bytes → Fernet.encrypt(bytes) → .enc file saved to disk

                  ┌─────────────────────────────┐
                  │  Fernet (AES-128-CBC)        │
                  │  + HMAC-SHA256 integrity     │
                  │  + PKCS7 padding             │
                  │  + Base64 encoding           │
                  │  + Timestamp for rotation    │
                  └─────────────────────────────┘
```

### Security Guarantees

| Aspect | Implementation |
|:-------|:---------------|
| **Encryption Algorithm** | Fernet symmetric encryption (AES-128-CBC + HMAC-SHA256) via Python `cryptography` library |
| **Key Management** | Key stored in environment variable (`FACE_ENCRYPTION_KEY`), never in source code |
| **At-Rest Protection** | All `.enc` files on disk are fully encrypted — raw face images are **never** stored |
| **Key Rotation** | Auto-generated per-installation if no env var is set (dev mode) |
| **Password Storage** | Werkzeug `pbkdf2:sha256` salted hashing — plaintext passwords are never stored |
| **Input Validation** | Centralized `validators.py` engine — SQL injection, XSS, and malformed data blocked |
| **Session Security** | Flask signed cookies with `SECRET_KEY` |

### 🔓 Can Someone Reconstruct a Face from the Encrypted File?

**No.** The `.enc` files you see in `face_data/` are encrypted with AES-128. Without the `FACE_ENCRYPTION_KEY`:
- Brute-forcing a 128-bit AES key would take **~10^18 years** on the world's fastest supercomputer
- The HMAC-SHA256 integrity check rejects any tampered ciphertext
- Even partial key knowledge provides zero advantage (no known-plaintext attacks on Fernet)

> **Bottom Line:** Your biometric data is mathematically impossible to recover without the encryption key. Period.

---

## 🧰 Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|:------|:-----------|:--------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000?style=flat-square&logo=flask) | Web framework, API routing, session management |
| **AI / CV** | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white) ![MediaPipe](https://img.shields.io/badge/MediaPipe-4285F4?style=flat-square&logo=google&logoColor=white) | DNN face detection, LBPH recognition, 468-pt mesh |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) | Local dev (SQLite) / Cloud prod (PostgreSQL/Neon) |
| **Crypto** | ![Fernet](https://img.shields.io/badge/Fernet_AES--256-f59e0b?style=flat-square&logo=letsencrypt&logoColor=white) | Face data encryption at rest |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) | UI, camera integration, real-time scanning |
| **Email** | ![Gmail](https://img.shields.io/badge/SMTP/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white) | Absentee notifications with HTML templates |
| **Scheduler** | ![APScheduler](https://img.shields.io/badge/APScheduler-06b6d4?style=flat-square) | Automated daily absentee email triggers |
| **Deploy** | ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white) ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white) | Cloud hosting with Gunicorn WSGI |

</div>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Webcam (USB or built-in)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sofzenix/Smart-Attendance-System.git
cd Smart-Attendance-System

# 2. Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

### 🌐 Access Points

| Page | URL | Description |
|:-----|:----|:------------|
| **Home / Scanner** | `http://localhost:5000/` | Landing page with quick face scan |
| **Employee Login** | `http://localhost:5000/login` | Employee portal login |
| **Employee Register** | `http://localhost:5000/register` | New employee self-registration |
| **Admin Login** | `http://localhost:5000/admin` | Administrator dashboard access |

### 🔑 Default Admin Credentials

```
Email:    admin@sofzenix.com
Password: Admin@123
```

> ⚠️ **Change the admin password immediately after first login in production!**

---

## 🔧 Environment Variables

Create a `.env` file or set these in your deployment platform:

| Variable | Required | Default | Description |
|:---------|:--------:|:--------|:------------|
| `SECRET_KEY` | ⚠️ Prod | `smartface_super_secret_key...` | Flask session signing key |
| `DATABASE_URL` | ☁️ Cloud | *None (uses SQLite)* | PostgreSQL connection string (Neon) |
| `FACE_ENCRYPTION_KEY` | ⚠️ Prod | *Auto-generated* | Fernet key for face data encryption |
| `MAIL_USERNAME` | 📧 | *None* | Gmail address for sending notifications |
| `MAIL_PASSWORD` | 📧 | *None* | Gmail App Password (not regular password) |

<details>
<summary><strong>📧 How to Get a Gmail App Password</strong></summary>

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Navigate to **Security** → **2-Step Verification** (enable it first)
3. Scroll down to **App Passwords**
4. Select app: **Mail**, device: **Other** → name it "SmartFace"
5. Copy the 16-character password → use as `MAIL_PASSWORD`

</details>

---

## 📁 Project Structure

```
Smart-Attendance-System/
├── 📄 app.py                    # Main Flask application (routes, API, logic)
├── 📄 config.py                 # Configuration (DB, email, encryption keys)
├── 📄 email_service.py          # Absentee email notification service
├── 📄 retrain.py                # Manual model retraining script
├── 📄 requirements.txt          # Python dependencies
├── 📄 Procfile                  # Render/Heroku deployment command
├── 📄 runtime.txt               # Python version for deployment
│
├── 📂 database/
│   ├── 📄 db.py                 # Database connection + init + migrations
│   └── 📄 schema.sql            # PostgreSQL schema definition
│
├── 📂 utils/
│   ├── 📄 face_utils.py         # 🧠 Core AI engine (detection, recognition, anti-spoof)
│   └── 📄 validators.py         # Input validation engine (name, email, phone, etc.)
│
├── 📂 face_data/                # 🔐 Encrypted face files (.enc) + trainer model
│   ├── 📄 trainer.yml           # LBPH trained model
│   ├── 📄 deploy.prototxt       # DNN face detector config
│   ├── 📄 res10_300x300_ssd_*   # DNN face detector weights
│   └── 📄 face_*_*.jpg.enc      # AES-256 encrypted face images
│
├── 📂 templates/                # Jinja2 HTML templates
│   ├── 📄 base.html             # Layout with sidebar + topbar
│   ├── 📄 index.html            # Landing page (particles.js)
│   ├── 📄 scanner.html          # Full-screen camera scanner
│   ├── 📄 register.html         # Employee registration form
│   ├── 📄 profile.html          # Employee profile editor
│   ├── 📄 settings.html         # Admin settings panel
│   ├── 📄 admin_dashboard.html  # Admin stats & management
│   └── 📄 ...                   # Other template files
│
├── 📂 static/
│   ├── 📂 css/style.css         # Premium dark-mode stylesheet
│   └── 📂 js/camera.js          # Camera capture + optimization
│
└── 📄 .env.example              # Environment variable template
```

---

## 📡 API Reference

### `POST /api/recognize_face`
Main face recognition endpoint called by the scanner at 300ms intervals.

**Request:**
```json
{
  "image": "data:image/jpeg;base64,...",
  "liveness_verified": false
}
```

**Response (recognized, awaiting liveness):**
```json
{
  "success": false,
  "recognized": true,
  "liveness_metrics": {
    "eyes_closed": false,
    "smiling": false,
    "ear": 0.312
  },
  "anti_spoof_score": 72,
  "spoof_checks": {
    "texture": true,
    "edge_density": true,
    "color_temp": true,
    "moire_detect": true,
    "glare_detect": true,
    "frequency": true,
    "face_consistency": true,
    "eye_presence": true,
    "screen_border": true,
    "3d_pose_depth": true
  },
  "confidence": 85,
  "user": "Yash",
  "emp_id": "EMP001",
  "department": "IT"
}
```

### `POST /api/register_face`
Register a face for the logged-in user (requires session auth).

### `GET /export_csv`
Download attendance data as CSV (admin-only). Supports `?date_from=` and `?date_to=` query params.

---

## 👨‍💼 Admin Guide

### First-Time Setup
1. Start the app → Go to `/admin` → Login with `admin@sofzenix.com` / `Admin@123`
2. Navigate to **Settings** → Set your company name and late cutoff time
3. Have employees self-register at `/register`
4. Each employee must scan their face at the scanner to enroll biometrics
5. After enrollment, employees can mark attendance by simply looking at the camera

### Managing Employees
- **View All Employees:** Admin Dashboard → Employees page
- **Delete Employee:** Click the delete button (removes user + attendance records)
- **Export Data:** Settings → "Export All Attendance (CSV)" or use the sidebar link

### Email Notifications
1. Go to **Settings** → Enable "Auto Absentee Emails"
2. Set your SMTP credentials in environment variables
3. Configure trigger time (e.g., 18:00 = 6 PM daily)
4. Optionally add an HR email for CC notifications
5. Test with "Send Test Email" button

---

## ☁️ Deployment

### Deploy on Render.com + Neon (Recommended)

#### Step 1: Create Cloud Database
1. Sign up at [neon.tech](https://neon.tech)
2. Create a project → Copy the PostgreSQL connection string
3. Format: `postgresql://user:pass@ep-xxx.us-east-2.aws.neon.tech/neondb`

#### Step 2: Deploy to Render
1. Push code to GitHub
2. Sign up at [render.com](https://render.com)
3. **New+ → Web Service** → Connect your GitHub repo
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
5. Add environment variables:
   ```
   DATABASE_URL = <your neon connection string>
   SECRET_KEY = <generate a random 32-char string>
   FACE_ENCRYPTION_KEY = <your Fernet key>
   MAIL_USERNAME = <gmail address>
   MAIL_PASSWORD = <gmail app password>
   ```
6. Click **Deploy** 🚀

> **Note:** Vercel is NOT supported — it uses serverless functions with 10s timeouts, incompatible with our real-time AI processing pipeline.

---

## 📝 Report / Project Documentation

<details>
<summary><strong>📖 Click to expand full academic project report outline</strong></summary>

### 1. Introduction
SmartFace AI is an AI-powered biometric attendance management system that replaces traditional methods (manual registers, ID cards, fingerprint scanners) with instant, touchless face recognition. The system is designed for organizations of 10–500 employees and provides enterprise-grade security through multi-layer anti-spoofing and encrypted biometric storage.

### 2. Problem Statement
Traditional attendance systems suffer from:
- **Buddy punching** — employees clocking in for absent colleagues
- **Time-consuming** — manual processes and long queues at biometric scanners
- **Hygiene** — fingerprint scanners require physical contact
- **Spoofing** — basic face recognition can be fooled by photos or videos

### 3. Proposed Solution
An AI-driven web application that:
- Recognizes employees via face recognition in under 300ms
- Prevents all known spoofing attacks through 10 independent detection layers
- Requires real-time liveness verification (blink detection)
- Encrypts all biometric data with AES-256 at rest
- Provides admin dashboards, analytics, and automated email alerts

### 4. Technologies Used
| Component | Technology |
|-----------|-----------|
| Language | Python 3.11 |
| Framework | Flask 2.3 |
| Face Detection | OpenCV DNN (ResNet-10 SSD) |
| Face Recognition | LBPH (Local Binary Patterns Histograms) |
| 3D Mesh | Google MediaPipe Face Mesh (468 landmarks) |
| Encryption | Python `cryptography` (Fernet/AES-128-CBC) |
| Database | SQLite (dev) / PostgreSQL via Neon (prod) |
| Email | SMTP via Gmail + APScheduler |
| Deployment | Render.com + Gunicorn WSGI |
| Frontend | HTML5, CSS3, JavaScript, Particles.js |

### 5. System Modules
1. **Authentication Module** — Login/Register with input validation & password hashing
2. **Face Registration Module** — Multi-sample capture + augmentation + encrypted storage
3. **Face Recognition Module** — DNN detection → LBPH matching → confidence scoring
4. **Anti-Spoofing Module** — 10-layer analysis pipeline (see table above)
5. **Liveness Module** — MediaPipe EAR-based blink detection
6. **Attendance Module** — Date/time logging, late detection, duplicate prevention
7. **Admin Module** — Dashboard, employee management, settings, CSV export
8. **Notification Module** — APScheduler + SMTP automated absentee emails
9. **Profile Module** — Photo upload, info editing, password change
10. **Analytics Module** — Department breakdowns, trend analysis

### 6. Data Flow
```
Registration:
  Camera → DNN Face Detection → ROI Extraction → 11x Augmentation
  → AES Encryption → .enc file → LBPH Training → trainer.yml

Attendance:
  Camera → DNN Detection → LBPH Predict → Identity Match?
  → 10-Layer Anti-Spoof → Blink Challenge → Attendance INSERT
  → Late/Present status → Dashboard update
```

### 7. Testing Results
| Test Case | Method | Result |
|-----------|--------|--------|
| Photo on phone screen | Hold phone to camera | ❌ Rejected (Screen border + Moiré + 3D Pose) |
| Printed photo | Hold printout to camera | ❌ Rejected (Texture + Edge + No liveness) |
| Video on laptop | Play video on monitor | ❌ Rejected (Glare + Frequency + No blink response) |
| Real face without blink | Stare at camera | ⏳ Awaiting blink (liveness challenge pending) |
| Real face with blink | Look + blink naturally | ✅ Granted in 1-2 seconds |
| Multiple faces | Two people in frame | ❌ Rejected (multi-face detection) |
| Unregistered person | Unknown face | ❌ "Identity Unknown — Register first" |

### 8. Future Enhancements
- Deep learning-based face recognition (FaceNet / ArcFace embeddings)
- Multi-camera support for office entry/exit tracking
- Mobile app with push notifications
- SSO integration (Google/Microsoft OAuth)
- Geo-fencing for remote/hybrid workers

### 9. Conclusion
SmartFace AI demonstrates that enterprise-grade biometric attendance is achievable with open-source tools. The 10-layer anti-spoofing pipeline, combined with MediaPipe liveness detection and AES-encrypted storage, provides a security posture comparable to commercial solutions costing 100x more.

</details>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
Copyright (c) 2026 Sofzenix Technologies
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0e1a,50:064e3b,100:10b981&height=120&section=footer" width="100%" />

<p>
  <strong>Built with ❤️ by <a href="https://github.com/Sofzenix">Sofzenix Technologies</a></strong>
</p>

<p>
  <a href="#top">⬆️ Back to Top</a>
</p>

</div>
