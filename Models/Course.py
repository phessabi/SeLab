class Course:
    def __init__(self, id_number: int, name: str):
        self.id = id_number
        self.name = name
        self._state = None
