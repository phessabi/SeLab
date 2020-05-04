class Course:
    def __init__(self, id_number: int, name: str, department):
        self.id = id_number
        self.name = name
        self.state = Course.State()
        self.department = department

    class State:
        def __init__(self):
            self._state = 'not presented'

        def set_presented(self):
            self._state = 'presented'

        def set_running(self):
            self._state = 'running'

        def set_not_presented(self):
            self._state = 'not presented'

        def is_presented(self):
            return self._state == 'presented'

        def is_running(self):
            return self._state == 'running'

        def is_not_presented(self):
            return self._state == 'not presented'
