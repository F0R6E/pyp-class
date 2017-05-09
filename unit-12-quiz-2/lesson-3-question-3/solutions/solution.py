class Student(object):
    def __init__(self, first_name, last_name, age, country="United States"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    @staticmethod
    def compatriot(one_student, other_student):
        return one_student.country == other_student.country
