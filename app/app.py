from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)