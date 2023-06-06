
class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        print(f'Created Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('John', 'Smith')
