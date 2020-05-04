import logging


class Person:
    def __init__(self, id_number: int, name: str):
        if not isinstance(id_number, int):
            raise TypeError('Person.id_number must be "int" given "' + str(type(id_number).__name__) + '" instead')
        self.id = id_number

        if not isinstance(name, str):
            logging.warn(' Person.name must be string... casting to string: ' + str(name))
        self.name = str(name)


