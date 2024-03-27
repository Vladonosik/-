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
        if len(self.grades) > 0:
            avg_grade = sum(sum(vals) for vals in self.grades.values()) / sum(
                len(vals) for vals in self.grades.values())
        else:
            avg_grade = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
    def avg_grade(self):
        total_grades = sum(len(vals) for vals in self.grades.values())
        if total_grades == 0:
            return 0
        total_scores = sum(sum(vals) for vals in self.grades.values())
        return total_scores / total_grades if total_grades > 0 else 0

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
        if self.grades:
            total_scores = sum(sum(vals) for vals in self.grades.values())
            total_grades = sum(len(vals) for vals in self.grades.values())

            avg_grade = total_scores / total_grades if total_grades > 0 else 0
        else:
            avg_grade = 0

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def avg_grade(self):
        total_grades = sum(len(vals) for vals in self.grades.values())
        if total_grades == 0:
            return 0
        total_scores = sum(sum(vals) for vals in self.grades.values())
        return total_scores / total_grades if total_grades > 0 else 0

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

student1 = Student('Alice', 'Cooper', 'female')
student2 = Student('Bob', 'Marley', 'male')

mentor1 = Mentor('John', 'Doe')
mentor2 = Mentor('Jane', 'Smith')

lecturer1 = Lecturer('Mike', 'Johnson')
lecturer2 = Lecturer('Emily', 'Davis')

reviewer1 = Reviewer('Kevin', 'Brown')
reviewer2 = Reviewer('Sarah', 'Green')

print(student1)
print(student2)

print(mentor1)
print(mentor2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

def avg_hw_grade(students, course_name):
    total_grade = 0
    total_students = 0
    for student in students:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
            total_students += len(student.grades[course_name])
    if total_students > 0:
        return total_grade / total_students
    return 0

def avg_lecture_grade(lecturers, course_name):
    total_grade = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades and lecturer.grades[course_name]:
            total_grade += sum(lecturer.grades[course_name])
            total_lecturers += len(lecturer.grades[course_name])
    if total_lecturers > 0:
        return total_grade / total_lecturers
    return 0

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

course_for_avg_grade = 'Python'

avg_hw = avg_hw_grade(students, course_for_avg_grade)
print(f"Средняя оценка за домашние задания по курсу '{course_for_avg_grade}': {avg_hw}")

avg_lecture = avg_lecture_grade(lecturers, course_for_avg_grade)
print(f"Средняя оценка за лекции по курсу '{course_for_avg_grade}': {avg_lecture}")