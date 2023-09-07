from database import Session, Student

def add_student(name):
    session = Session()
    student = Student(name=name)
    session.add(student)
    session.commit()
    session.close()

def get_student_details(student_id):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    session.close()
    return student

def list_students():
    session = Session()
    students = session.query(Student).all()
    session.close()
    return students
