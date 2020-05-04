from Models.Person import Person
from Models.TakenCourse import TakenCourse


class Professor(Person):
    def __init__(self, id_number: int, name: str, room_no: int, lab_no: int):
        super(Professor, self).__init__(id_number, name)
        self.student_list = []
        self.project_list = []
        self.room_no = room_no
        self.lab_no = lab_no

        self._active_courses = {}  # {CourseName: list of TakenCourse}

    def present_course(self, course):
        self._active_courses[course.name] = course


    @property
    def salary(self):
        students_multiplier = 3000000
        courses_multiplier = 3000000
        projects_multiplier = 3000000
        constant_salary = 5000000

        return \
            len(self.student_list) * students_multiplier + \
            len(self._active_courses) * courses_multiplier + \
            len(self.project_list) * projects_multiplier + \
            constant_salary
