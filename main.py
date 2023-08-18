class Person:
    def __init__(self, name, age, surname):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} {self.age}"


class Teacher(Person):
    def __init__(self, name, age, surname, subject):
        super().__init__(name, age, surname)
        self.subject = subject

    def __str__(self):
        return f"{self.name} {self.age} {self.surname} {self.subject}"


class Student(Person):
    def __init__(self, name, age, surname, grade):
        super().__init__(name, age, surname)
        self.grade = grade

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.grade}"


class Subject:
    def __init__(self, name, code, assessment):
        self.name = name
        self.code = code
        self.assessment = assessment

    def __str__(self):
        return f"{self.name} {self.code} {self.assessment}"


class Academy:
    def __init__(self, name, location):
        self.name = name
        self.location = location

        self.list_teachers = []
        self.list_students = []
        self.list_subjects = []

    def add_list_teachers(self, teachers):
        self.list_teachers.append(teachers)

    def add_list_student(self, student):
        self.list_teachers.append(student)

    def add_list_subject(self, subject):
        self.list_teachers.append(subject)

    def __str__(self):
        return f"{self.name} {self.location}" \
               f"\nTeachers: {', '.join(str(teacher) for teacher in self.list_teachers)}" \
               f"\nStudents: {', '.join(str(student) for student in self.list_students)}" \
               f"\nSubjects: {', '.join(str(subject) for subject in self.list_subjects)}"


math_teacher = Teacher("John", "Doe", 35, "Mathematics")
history_teacher = Teacher("Jane", "Smith", 42, "History")

student1 = Student("Alice", "Johnson", 18, "Senior")
student2 = Student("Bob", "Williams", 17, "Junior")

math_subject = Subject("Mathematics", "MATH117", 2)
history_subject = Subject("History", "HIST117", 3)

academy = Academy("Example Academy", "London")

academy.add_list_teachers(math_teacher)
academy.add_list_teachers(history_teacher)
academy.add_list_student(student1)
academy.add_list_student(student2)
academy.add_list_subject(math_subject)
academy.add_list_subject(history_subject)

print(academy)
