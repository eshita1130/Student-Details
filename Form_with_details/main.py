from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["B_Tech"]
collection = db["CSE"]

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    name = request.form["name"]
    registration_no = request.form["registration_no"]
    roll_no = request.form["roll_no"]
    school = request.form["school"]
    program = request.form["program"]
    admission_year = request.form["admission_year"]
    address = request.form["address"]
    gender = request.form["gender"]
    email = request.form["email"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    collection.insert_one(
        {"name": name, "registration_no": registration_no, "roll_no": roll_no, "school": school, "program": program,
         "admission_year": admission_year, "address": address, "email": email, "phone": phone, "dob": dob})
    data = collection.find()
    return render_template("successLogin.html", data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Eshita' and password == '1105':
            return redirect(url_for('dashboard'))
        else:
            return render_template('admin.html', error='Invalid credentials')
    return render_template('admin.html', error=None)


@app.route('/dashboard')
def dashboard():
    data = collection.find()
    return render_template('dashboard.html', data=data)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    return render_template("admin.html")


if __name__ == '__main__':
    app.run()
