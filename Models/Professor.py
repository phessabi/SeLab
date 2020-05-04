from Models.Person import Person


class Professor(Person):
    def __init__(self, id_number: int, name: str, room_no: int, lab_no: int):
        super(Professor, self).__init__(id_number, name)
        self.course_list = []
        self.student_list = []
        self.project_list = []
        self.room_no = room_no
        self.lab_no = lab_no

