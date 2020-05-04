from Models.Person import Person
from Models.TakenCourse import TakenCourse


class Student(Person):
    def __init__(self, id_number: int, name: str, department):
        super(Student, self).__init__(id_number, name)
        self._taken_courses = {}  # {CourseName: list of TakenCourse}
        self. department = department
        self.on_semester = True

    def grade(self, course_name: str) -> float:
        """
        :return: returns grade of the given course, None if course isn't finished yet
        """
        if course_name not in self._taken_courses:
            raise KeyError("course: " + str(course_name) + " was not taken by student:" + self.name)
        return self._taken_courses[course_name][-1].grade

    def enroll(self, course, professor):
        if course.name not in self._taken_courses:
            # check course restrictions
            self._taken_courses[course.name] = [TakenCourse(self, professor, course)]
        elif  self.on_semester==False:
            raise AssertionError("Student : "+str(self.name)+" Has not enrolled in this semester.")

        elif course.department != self.department:
            raise AssertionError("Student's department is "+str(self.department)+" whereas course's department is "+str(course.department))
        elif self._taken_courses[course.name][-1].grade is None:
            raise AssertionError("Course: " + str(course.name) + " is already taken by Student:" + str(self.name))
        elif self._taken_courses[course.name][-1].grade >= 10:
            raise AssertionError("Course: " + str(course.name) + " has been passed by Student:" + str(self.name) +
                                 " with grade:" + str(self._taken_courses[course.name][-1].grade))
        else:
            # student is taking a course he failed once
            self._taken_courses[course.name].append(TakenCourse(self, professor, course))

    def finish(self, course_name, grade):
        if course_name not in self._taken_courses:
            raise KeyError("Course:" + str(course_name) + " was not taken by Student:" + str(self.name))
        else:
            self._taken_courses[course_name][-1].grade = grade

    def enroll_semester(self):
        self.on_semester = True
    def w_semester(self):
        self.on_semester = False
