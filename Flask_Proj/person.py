# person.py: Person & Response model classes

class Person:
    """
        Person model class
    """

    def __init__(self, person_id, name, age):
        self._person_id = person_id
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id


class Response:
    """
    REST API response class
    """

    def __init__(self, status=None, message=None):
        self._status = status
        self._message = message

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
