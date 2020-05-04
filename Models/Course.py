class Course:
    def __init__(self, id_number: int, name: str):
        self.id = id_number
        self.name = name
        self.state = Course.State()

    class State:
        def __init__(self):
            self._state = 'not represented'

        def set_represented(self):
            self._state = 'represented'

        def set_running(self):
            self._state = 'running'

        def set_not_represented(self):
            self._state = 'not represented'

        def is_represented(self):
            return self._state == 'represented'

        def is_running(self):
            return self._state == 'running'

        def is_not_represented(self):
            return self._state == 'not represented'
