class Student:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name}  {self.surname}'


class Group:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return '\n'.join(map(str, self.students))


st_1 = Student('Ivan', 'Ivanov')
st_2 = Student('Stepan', 'Stepanenko')
st_3 = Student('Roman', 'Romanenko')

group = Group()
group.add_student(st_1)
group.add_student(st_2)
group.add_student(st_3)
group.add_student(st_3)
group.add_student(st_3)
group.add_student(st_3)

print(group)