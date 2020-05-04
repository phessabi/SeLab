from Models.Person import Person


class Student(Person):
    def __init__(self, id_number: int, name: str):
        super(Student, self).__init__(id_number, name)
