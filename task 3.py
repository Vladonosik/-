class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(vals) for vals in self.grades.values()) / sum(len(vals) for vals in self.grades.values())
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def avg_grade(self):
        return sum(sum(vals) for vals in self.grades.values()) / sum(len(vals) for vals in self.grades.values())

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = sum(sum(vals) for vals in self.grades.values()) / sum(len(vals) for vals in self.grades.values())
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def avg_grade(self):
        return sum(sum(vals) for vals in self.grades.values()) / sum(len(vals) for vals in self.grades.values())

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades = {'Python': [8, 9, 10], 'Git': [10]}

some_lecturer = Lecturer('John', 'Doe')
some_lecturer.courses_attached = ['Python', 'Git']
some_lecturer.grades = {'Python': [9, 10, 9], 'Git': [8, 7]}

some_reviewer = Reviewer('Alice', 'Smith')
some_reviewer.courses_attached = ['Python', 'Git']

print(some_student)
print(some_lecturer)
print(some_reviewer)

print(some_student < some_lecturer)