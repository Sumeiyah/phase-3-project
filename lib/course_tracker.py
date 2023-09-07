from database import Session, Course

def add_course(name):
    session = Session()
    course = Course(name=name)
    session.add(course)
    session.commit()
    session.close()

def get_course_details(course_id):
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    session.close()
    return course

def list_courses():
    session = Session()
    courses = session.query(Course).all()
    session.close()
    return courses
