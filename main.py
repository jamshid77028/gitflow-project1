class User:

    def __init__(self, first_name, last_name):
        self.__id = self.__generate__id()
        self.first_name = first_name
        self.last_name = last_name


    def __generate_id(self):
        from uuid import uuid4

        return str(uuid4())


    @property
    def id(self):
        return self.__id

