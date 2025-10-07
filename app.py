import os
from flask import Flask, render_template, request, redirect, url_for, send_file, session, flash, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import gridfs
import io

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')  # Required for session management

# MongoDB connection
app.config["MONGO_URI"] = os.environ.get('MONGODB_URI', "mongodb://localhost:27017/study_portal")
mongo = PyMongo(app)
fs = gridfs.GridFS(mongo.db)

# Authentication decorator for admin-only routes
def admin_required(f):
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Please login as admin to access this page', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Home (Welcome page)
@app.route("/")
def home():
    return render_template("welcome.html")

# Semesters page
@app.route("/semesters")
def semesters():
    return render_template("sem3.html")

# Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Login (Admin only)
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Fixed admin credentials
        if username == "Pratik" and password == "@Pratik9890":
            session['admin_logged_in'] = True
            session['username'] = username
            flash('Successfully logged in as admin!', 'success')
            return redirect(url_for("upload"))  # redirect to upload page after login
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)

# Logout route
@app.route("/logout")
def logout():
    session.pop('admin_logged_in', None)
    session.pop('username', None)
    flash('Successfully logged out', 'success')
    return redirect(url_for('home'))

# Upload PDF (Admin Only)
@app.route("/upload", methods=["GET", "POST"])
@admin_required
def upload():
    if request.method == "POST":
        file = request.files["pdf"]
        semester = request.form.get("semester")
        subject = request.form.get("subject")

        if file and file.filename.endswith(".pdf"):
            file_id = fs.put(file, filename=file.filename)
            mongo.db.files.insert_one({
                "file_id": file_id,
                "filename": file.filename,
                "semester": semester,
                "subject": subject
            })
            flash('PDF uploaded successfully!', 'success')
            return redirect(url_for("view_pdfs"))
        else:
            flash('Please select a valid PDF file', 'error')
    return render_template("upload.html")

@app.route("/pdfs")
def view_pdfs():
    files = list(mongo.db.files.find())
    # Convert ObjectId to string
    for f in files:
        f["file_id"] = str(f["file_id"])
    return render_template("view_pdfs.html", files=files)

# View all subjects for a specific semester
@app.route("/pdfs/<semester>")
def view_semester_subjects(semester):
    # Get all unique subjects for this semester
    subjects = mongo.db.files.distinct("subject", {"semester": semester})
    semester_info = {
        "SEM1": {"name": "Semester 1", "subjects": ["M1", "Physics", "BEE", "FPL", "EG"]},
        "SEM2": {"name": "Semester 2", "subjects": ["Chemistry", "EM", "M2", "PPS", "BXE"]},
        "SEM3": {"name": "Semester 3", "subjects": ["DM", "LDCO", "DSA", "OOPS", "BCN"]},
        "SEM4": {"name": "Semester 4", "subjects": ["M3", "PA", "DBMS", "CG", "SE"]},
        "SEM5": {"name": "Semester 5", "subjects": ["OS", "TOC", "ML", "HCI", "ADMBS"]},
        "SEM6": {"name": "Semester 6", "subjects": ["CNS", "DSBDA", "WAD"]},
        "SEM7": {"name": "Semester 7", "subjects": ["ISR", "SPM", "DL", "Mobile Computing", "Wireless Communication"]},
        "SEM8": {"name": "Semester 8", "subjects": ["DS", "STARTUP", "Blockchain Technology", "NLP"]}
    }

    semester_data = semester_info.get(semester, {"name": semester, "subjects": []})

    # Get file counts for each subject in this semester
    subject_files = {}
    for subject in semester_data["subjects"]:
        count = mongo.db.files.count_documents({"semester": semester, "subject": subject})
        subject_files[subject] = count

    return render_template("semester_subjects.html",
                         semester=semester,
                         semester_name=semester_data["name"],
                         subjects=semester_data["subjects"],
                         subject_files=subject_files)

# View PDFs for a specific semester + subject
@app.route("/pdfs/<semester>/<subject>")
def view_subject_pdfs(semester, subject):
    files = list(mongo.db.files.find({"semester": semester, "subject": subject}))
    for f in files:
        f["file_id"] = str(f["file_id"])
    return render_template("subject_pdfs.html", files=files, semester=semester, subject=subject)

# Download/View PDF - Public Access
@app.route("/pdf/<file_id>")
def get_pdf(file_id):
    try:
        file_obj = fs.get(ObjectId(file_id))
        return send_file(io.BytesIO(file_obj.read()), download_name=file_obj.filename, mimetype="application/pdf")
    except Exception as e:
        flash('File not found or corrupted', 'error')
        return redirect(url_for('view_pdfs'))


if __name__ == "__main__":
    app.run(debug=True)
