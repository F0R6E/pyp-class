class Student(object):
    def __init__(self, first_name, last_name, age, country="United States"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} ({}) from {}".format(self.full_name, self.age, self.country)

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age
