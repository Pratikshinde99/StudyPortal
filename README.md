# StudyPortal

# 🎓 SPPU Study Material Portal

> **ADBMS Mini Project**  
> A complete study portal for **Savitribai Phule Pune University (SPPU)** IT students — built using **Flask**, **MongoDB**, and **GridFS**.


## 📘 Project Overview

The **SPPU Study Material Portal** is a web-based platform designed for **SPPU Information Technology students** to access organized study materials, previous year question papers, and resources for all **8 semesters**.  
It demonstrates **Advanced Database Management System (ADBMS)** concepts, **Flask web development**, **MongoDB integration**, and **GridFS file storage**.

This project provides a **real-world use case** of database-backed web applications with **secure admin authentication** and **responsive dark-themed UI**.

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python (Flask Framework) |
| **Database** | MongoDB (with GridFS for file storage) |
| **Authentication** | Session-based Admin Authentication |
| **Styling** | Dark Theme with Glassmorphism and Animations |

---

## ✨ Features

### 👨‍🎓 Student Features
- 🏠 **Homepage** with modern dark theme and smooth animations  
- 📚 **Semester-wise material access** (SEM1–SEM8)  
- 📑 **Subject-wise organization** for easy navigation  
- 📂 **File metadata display** – upload date, size, and name  
- ⬇️ **Direct PDF download** from MongoDB GridFS  
- 📱 **Fully responsive design** (mobile-first)  

### 👨‍💼 Admin Features
- 🔐 **Secure Admin Login** (Session-based)  
- 📤 **Upload Study Materials** (semester + subject + file)  
- 🧾 **Manage all uploads** with filters  
- ⚠️ **File validation** (PDF only)  
- 💬 **Flash messages** for feedback (success/error)  
- 🚪 **Session logout** for security  

---

## 🧱 System Architecture

```text
┌─────────────────┐              ┌─────────────────┐    ┌─────────────────┐
│   Flask Web     │   ◄──────►   │   MongoDB DB     │    │   GridFS File    │
│   Application   │              │   (Metadata)     │    │   Storage        │
└─────────────────┘              └─────────────────┘    └─────────────────┘
                  │                       │
                 ▼                        ▼
┌─────────────────┐              ┌─────────────────┐
│   HTML/CSS/JS   │              │   PDF Files      │
│   Templates     │              │   (GridFS)       │
└─────────────────┘              └─────────────────┘


**🗂️ Folder Structure**
study-portal/
│
├── templates/              # HTML templates (home, login, upload, semesters)
├── static/                 # CSS, JS, images
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── ...                     # Other helper files


💾 MongoDB Collections
📂 files (GridFS metadata)
{
  "_id": ObjectId,
  "filename": "dbms_notes.pdf",
  "semester": "SEM4",
  "subject": "DBMS",
  "upload_date": "2025-10-06T10:00:00",
  "file_id": ObjectId("GridFS reference")
}



🌐 Application Routes
Route	                          Method             	Description
  /	                             GET	                 Home page
/semesters                     	 GET	                 List all semesters
/pdfs/<semester>	               GET	                 List subjects under selected semester
/pdfs/<semester>/<subject>	     GET                   View files for selected subject
/pdf/<file_id>	                 GET	                 Download specific PDF
/login	                         GET/POST	             Admin login
/upload	                         GET/POST	             Upload new materials
/pdfs	                           GET	                 Admin dashboard to view files
/logout	                         GET	                 Logout admin session


🧰 Installation & Setup Guide
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/sppu-study-material-portal.git
cd sppu-study-material-portal

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Start MongoDB
Ensure MongoDB is running locally
OR configure MongoDB Atlas connection string in your code.

6️⃣ Run the Application
python app.py

7️⃣ Open in Browser
🔗 http://localhost:5000

⚙️ System Requirements
🐍 Python 3.8+
🍃 MongoDB (Local or Atlas)
🌐 Modern Web Browser
💻 Internet connection (if using MongoDB Atlas)

🖼️ Screenshots
Page	Description
🏠 Home Page	Welcome page with dark theme
📚 Semester List	All 8 semesters organized
📄 Subject Page	Subject-wise file listing
🔐 Admin Login	Secure login interface
📤 Upload Page	Admin upload dashboard

(Add actual screenshots in /assets folder and embed them here later)

🎨 UI/UX Design
🌙 Dark Theme (Eye-friendly for study sessions)
💠 Glassmorphism Cards (Modern appearance)
🌀 Smooth Animations (Hover and transitions)
📱 Mobile-First Responsive Design
🧭 Intuitive Navigation & Clear Layout


🎨 Color Palette
Purpose	Color
Background	#0a0a0f → #12121a
Primary	#6366f1 (Indigo)
Secondary	#14b8a6 (Teal)
Accent	#f59e0b (Amber)
Text	White / Gray


🔒 Security Features
Session-based authentication
Protected admin routes
Automatic logout on session expiry
File validation (PDF only)
GridFS file storage (no direct filesystem access)


📚 Educational Value
✅ Demonstrates ADBMS concepts using MongoDB & GridFS
✅ Implements Flask web application development
✅ Covers CRUD operations, file handling, and authentication
✅ Built with modern UI design principles


📊 Learning Outcomes
Concept	Implementation
Database Management	MongoDB CRUD + GridFS
Backend Development	Flask routes, sessions, flash messages
Frontend Development	HTML, CSS, JS with dark theme
Authentication	Session-based admin login
File Handling	PDF uploads & downloads with GridFS
UI/UX Design	Responsive, glassmorphic dark theme


☁️ Deployment (Optional)You can deploy:
Backend (Flask): Render, PythonAnywhere
Database (MongoDB): MongoDB Atlas
Then configure the connection string in app.py.

📜 License:
This project is created for academic and learning purposes.
You may use and modify it with proper credit to the original author.

👨‍💻 Developer: 
👤 Pratik Shinde
📧 Email: ps175581@gmail.com

🔗 GitHub: https://github.com/Pratikshinde99
