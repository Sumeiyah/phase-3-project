from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    grades = relationship("Grade", back_populates="student")

# Define Course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    grades = relationship("Grade", back_populates="course")
    
# Define Grade model
class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    assignment_grade = Column(Float)
    exam_grade = Column(Float)
    coursework_grade = Column(Float)

    student = relationship("Student", back_populates="grades")
    course = relationship("Course", back_populates="grades")

# Create database connection
engine = create_engine('sqlite:///student_grade_tracker.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
