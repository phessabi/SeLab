import datetime


class TakenCourse:
    def __init__(self, student, professor, course):
        """
        :param student: Student Object
        :param professor: Professor Object
        :param course: Course Object
        """
        self.student = student
        self.professor = professor
        self.course = course
        self.grade = None
        self.date = datetime.datetime.now().date()

    def set_grade(self, grade: float):
        self.grade = grade
