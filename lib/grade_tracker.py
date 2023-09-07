from database import Session, Grade, Student, Course

def add_grade(student_id, course_id, assignment_grade, exam_grade, coursework_grade):
    session = Session()
    grade = Grade(student_id=student_id, course_id=course_id, assignment_grade=assignment_grade,
                  exam_grade=exam_grade, coursework_grade=coursework_grade)
    session.add(grade)
    session.commit()
    session.close()

def get_student_grades(student_id, course_id):
    session = Session()
    grades = session.query(Grade).filter_by(student_id=student_id, course_id=course_id).first()
    session.close()
    return grades

def calculate_course_grade(course_id):
    session = Session()
    students = session.query(Student).all()
    total_assignment_weight = 0.4
    total_exam_weight = 0.4
    total_coursework_weight = 0.2

    course_grades = [] 

    course = session.query(Course).filter_by(id=course_id).first()
    if not course:
        session.close()
        return None

    for student in students:
        student_id = student.id
        grades = session.query(Grade).filter_by(student_id=student_id, course_id=course_id).first()

        if grades:
            assignment_grade = grades.assignment_grade
            exam_grade = grades.exam_grade
            coursework_grade = grades.coursework_grade

            overall_grade = (assignment_grade * total_assignment_weight +
                             exam_grade * total_exam_weight +
                             coursework_grade * total_coursework_weight)
            
            course_grades.append((student.name, overall_grade))

    session.close()

    return course_grades