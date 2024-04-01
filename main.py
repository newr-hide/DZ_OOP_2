class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def teacher_assessment(self, lecturer, course, rating):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.ratings:
                lecturer.ratings[course] += [rating]
            else:
                lecturer.ratings[course] = [rating]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def aver_grade(self):
        k = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                k += j
                count += 1
        return k / count

    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self.aver_grade()}\n{' '.join(self.courses_in_progress)}\nЗавершенный курс: {' '.join(self.finished_courses)}"

class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname,courses_attached)
        self.ratings = {}
    def aver_rating(self):
        k = 0
        count = 0
        for i in self.ratings.values():
            for j in i:
                k += j
                count += 1
                total = k / count
        return round(total, 2)
    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self.aver_rating()}"

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"{self.name}\n{self.surname}"

roma_student = Student('Roma', 'Evanov', 'M')
miha_student = Student("Misha", "Koh", "M")
roma_student.courses_in_progress += ['Python']
roma_student.courses_in_progress += ['GIT']
roma_student.finished_courses += ["Введение в программирование"]
mentor_reviewer_1 = Reviewer('Vlad', 'Buduk', ["Python","GIT"])
mentor_reviewer_2 = Reviewer("Olesya","Berezina",["Java","GIT"])
mentor_lecturer_1 = Lecturer("Petr", "Wedhin", ["Python", "GIT"])
mentor_lecturer_2 = Lecturer("Afanasyi","Letin",["Java","GIT"])
roma_student.teacher_assessment(mentor_lecturer_1, "Python", 10)
roma_student.teacher_assessment(mentor_lecturer_1, "Python", 6)
miha_student.teacher_assessment(mentor_lecturer_1, "GIT", 1)
roma_student.teacher_assessment(mentor_lecturer_1, "GIT", 10)
roma_student.teacher_assessment(mentor_lecturer_2, "GIT", 4)
miha_student.teacher_assessment(mentor_lecturer_2, "GIT", 3)
miha_student.finished_courses += ["Java"]
miha_student.courses_in_progress += ["Python"]
miha_student.courses_in_progress += ["GIT"]

mentor_reviewer_1.rate_hw(roma_student, 'Python', 5)
mentor_reviewer_1.rate_hw(roma_student, 'GIT', 3)
mentor_reviewer_1.rate_hw(roma_student, 'GIT', 1)
mentor_reviewer_1.rate_hw(roma_student, 'GIT', 10)
mentor_reviewer_2.rate_hw(roma_student, "GIT", 5)
mentor_reviewer_1.rate_hw(miha_student, "Python", 3)
#print(mentor_lecturer_2)
# print(mentor_lecturer_1)
# print(roma_student)
# print(miha_student)
