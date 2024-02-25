from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://reginafera13:102297@localhost/school' 

db = SQLAlchemy(app)

class Students(db.Model): # table == Model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    
class Teachers(db.Model): # table == Model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    
class Subjects(db.Model): # table == Model
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255))

@app.route('/api/v1/students', methods=['GET'])
def get_all_students():
    students = Students.query.all()
    json_students = []
    for stud in students:
        # Fetch subject name
        subject = Subjects.query.filter_by(id=stud.subject).first()
        subject_name = subject.subject if subject else None
        
        # Fetch teacher name
        teacher = Teachers.query.filter_by(subject=stud.subject).first()
        teacher_name = f"{teacher.first_name} {teacher.last_name}" if teacher else None
        
        # Construct JSON response
        json_student = {
            'id': stud.id,
            'first_name': stud.first_name,
            'last_name': stud.last_name,
            'age': stud.age,
            'class': {
                'subject': subject_name,
                'teacher': teacher_name
            }
        }
        json_students.append(json_student)
    
    response = jsonify(json_students)
    return response

@app.route('/api/v1/teachers', methods=['GET'])
def get_all_teachers():
    teachers = Teachers.query.all()
    json_teachers = []
    for teach in teachers:
        # Fetch subject name
        subject = Subjects.query.filter_by(id=teach.subject).first()
        subject_name = subject.subject if subject else None
        
        # Fetch list of student names
        students = Students.query.filter_by(subject=teach.subject).all()
        student_names = [f"{student.first_name} {student.last_name}" for student in students]
        
        # Construct JSON response
        json_teacher = {
            'id': teach.id,
            'first_name': teach.first_name,
            'last_name': teach.last_name,
            'age': teach.age,
            'subject': {
                'subject': subject_name,
                'students': student_names
            }
        }
        json_teachers.append(json_teacher)
    
    response = jsonify(json_teachers)
    return response

@app.route('/api/v1/subjects', methods=['GET'])
def get_all_subjects():
    subjects = Subjects.query.all()
    json_subjects = []
    for subj in subjects:
        # Fetch teacher name for each subject
        teacher = Teachers.query.filter_by(subject=subj.id).first()
        teacher_name = f"{teacher.first_name} {teacher.last_name}" if teacher else None

        # Fetch student names enrolled in each subject
        students = Students.query.filter_by(subject=subj.id).all()
        student_names = [f"{student.first_name} {student.last_name}" for student in students]

        # Construct JSON response for each subject
        json_subject = {
            'id': subj.id,
            'subject': subj.subject,
            'teacher_name': teacher_name,
            'students': student_names
        }
        json_subjects.append(json_subject)

    response = jsonify(json_subjects)
    return response

app.run(debug=True)