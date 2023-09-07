from database import Session, Grade, Course, Student 

def generate_course_report(course_id):
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        print(f"Report for Course: {course.name}")
        grades = session.query(Grade).filter_by(course_id=course_id).all()
        if grades:
            for grade in grades:
                student = session.query(Student).filter_by(id=grade.student_id).first()
                if student:
                    print(f"Student: {student.name}")
                    print(f"Assignment Grade: {grade.assignment_grade}")
                    print(f"Exam Grade: {grade.exam_grade}")
                    print(f"Coursework Grade: {grade.coursework_grade}")
                    print("\n")
        else:
            print("No grades found for this course.")
    else:
        print("Course not found.")
    session.close()

def calculate_class_averages(course_id):
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        print(f"Class Averages for Course: {course.name}")
        grades = session.query(Grade).filter_by(course_id=course_id).all()
        if grades:
            assignment_total = 0
            exam_total = 0
            coursework_total = 0
            total_students = len(grades)

            for grade in grades:
                assignment_total += grade.assignment_grade
                exam_total += grade.exam_grade
                coursework_total += grade.coursework_grade

            assignment_avg = assignment_total / total_students
            exam_avg = exam_total / total_students
            coursework_avg = coursework_total / total_students

            print(f"Assignment Average: {assignment_avg}")
            print(f"Exam Average: {exam_avg}")
            print(f"Coursework Average: {coursework_avg}")
        else:
            print("No grades found for this course.")
    else:
        print("Course not found.")
    session.close()
