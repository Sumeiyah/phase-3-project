import click
from student_tracker import add_student, get_student_details, list_students
from course_tracker import add_course, get_course_details, list_courses
from grade_tracker import add_grade, get_student_grades, calculate_course_grade
from report_generator import generate_course_report, calculate_class_averages

@click.group()
def cli():
    """Student Grade Tracker CLI"""
    pass

@cli.command()
@click.argument('name')
def add_student_cli(name):
    add_student(name)
    click.echo(f"Added student: {name}")

@cli.command()
@click.argument('student_id', type=int)
def get_student_cli(student_id):
    student = get_student_details(student_id)
    if student:
        click.echo(f"Student ID: {student.id}, Name: {student.name}")
    else:
        click.echo("Student not found.")

@cli.command()
def list_students_cli():
    students = list_students()
    click.echo("List of students:")
    for student in students:
        click.echo(f"Student ID: {student.id}, Name: {student.name}")

@cli.command()
@click.argument('name')
def add_course_cli(name):
    add_course(name)
    click.echo(f"Added course: {name}")

@cli.command()
@click.argument('course_id', type=int)
def get_course_cli(course_id):
    course = get_course_details(course_id)
    if course:
        click.echo(f"Course ID: {course.id}, Name: {course.name}")
    else:
        click.echo("Course not found.")

@cli.command()
def list_courses_cli():
    courses = list_courses()
    click.echo("List of courses:")
    for course in courses:
        click.echo(f"Course ID: {course.id}, Name: {course.name}")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
@click.argument('assignment_grade', type=float)
@click.argument('exam_grade', type=float)
@click.argument('coursework_grade', type=float)
def add_grade_cli(student_id, course_id, assignment_grade, exam_grade, coursework_grade):
    add_grade(student_id, course_id, assignment_grade, exam_grade, coursework_grade)
    click.echo("Grade added successfully.")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
def get_grades_cli(student_id, course_id):
    grades = get_student_grades(student_id, course_id)
    if grades:
        click.echo(f"Student ID: {grades.student_id}, Course ID: {grades.course_id}")
        click.echo(f"Assignment Grade: {grades.assignment_grade}")
        click.echo(f"Exam Grade: {grades.exam_grade}")
        click.echo(f"Coursework Grade: {grades.coursework_grade}")
    else:
        click.echo("Grades not found.")

@cli.command()
@click.argument('course_id', type=int)
def calculate_course_grade_cli(course_id):
    calculate_course_grade(course_id)
    click.echo("Course grades calculated.")

@cli.command()
@click.argument('course_id', type=int)
def generate_report_cli(course_id):
    generate_course_report(course_id)
    click.echo("Report generated.")

@cli.command()
@click.argument('course_id', type=int)
def calculate_averages_cli(course_id):
    calculate_class_averages(course_id)
    click.echo("Class averages calculated.")

if __name__ == '__main__':
    cli()
