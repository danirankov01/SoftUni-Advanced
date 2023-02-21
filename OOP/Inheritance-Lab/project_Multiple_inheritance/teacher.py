from project_Multiple_inheritance.employee import Employee
from project_Multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
    