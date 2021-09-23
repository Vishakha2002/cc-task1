from flask import Flask , redirect, url_for, render_template, request, flash
from student_form import StudentSearchForm, StudentAddForm
from flask_sqlalchemy import SQLAlchemy

app= Flask (__name__)
app.secret_key = 'sdfgsdfgsdf'
# 1IrhoLpcKCjpAxza
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
# export GOOGLE_APPLICATION_CREDENTIALS=/Users/vtyagi/Desktop/high-service-326703-b94e96aa2d3c.json
# We need to make sure that we are running ./cloud_sql_proxy -instances=high-service-326703:us-central1:firstapp=tcp:5432
# to connect to our Postgress SQL.
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:root123@127.0.0.1:5432/webapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    """"""
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    mailing_address = db.Column(db.String)
    gpa = db.Column(db.Integer)



@app.route("/add", methods=['GET', 'POST'])
def add():
    student_info = StudentAddForm(request.form)
    if request.method == 'POST':
        return add_student(student_info)
    return render_template('addstudent.html', form=student_info)

@app.route("/addstudent")
def add_student(student_info):
    response = None
    # print(f"Keshav Student data here {student_info.data}")
    info = student_info.data
    try:
        u = Student(first_name=info['first_name'],
                    last_name=info['last_name'],
                    email=info['email'],
                    mailing_address=info['mailing_address'],
                    gpa=info['gpa'])
        db.session.add(u)
        db.session.commit()
        flash(f"User {info['first_name']} {info['last_name']} has been added", "success")
        return redirect(url_for('add'))
    except Exception as exc:
        response = f"Unable to add student due to {str(exc)}"
        flash(response, "failure")

    return render_template('addstudent.html', form=student_info)


@app.route("/view")
def view_all_student():
    response = []
    result = None
    error = None
    try:
        result = Student.query.all()
        for item in result:
            print(item.id, item.first_name)
            response.append({'ID': item.id, "First Name":item.first_name, "Last Name": item.last_name, "EMAIL": item.email, "Mailing Address": item.mailing_address, "GPA": item.gpa})
    except Exception as exc:
        error = f"Unable to fetch all the Students from DB. Reason: {str(exc)}"
    

    return render_template('viewallstudent.html', response=response, error=error)

@app.route("/", methods=['GET', 'POST'])
def index():
    search = StudentSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    """
    search based on a selector
    """
    results = []
    result = None
    print(f"Keshav Search here {search.data}")
    search_string = search.data['search']

    if not search_string:
        flash('Please enter a value')
        return redirect('/')
    elif search.data['select'] == 'id' and search_string:
        result = db.session.query(Student).filter(Student.id == int(search_string))
    elif search.data['select'] == 'first_name' and search_string:
        result = db.session.query(Student).filter(Student.first_name == search_string)
    elif search.data['select'] == 'last_name' and search_string:
        result = db.session.query(Student).filter(Student.last_name == search_string)
    if result:
        for item in result:
            print(item.id, item.first_name)
            results.append({'ID': item.id, "First Name":item.first_name, "Last Name": item.last_name, "EMAIL": item.email, "Mailing Address": item.mailing_address, "GPA": item.gpa})

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        print("Came here")
        # display results
        return render_template('index.html', data=results, form=search)

if __name__ == "__main__":
    db.create_all()
    app.run()