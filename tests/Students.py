class Students:
    def __init__(self, name, age, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

def get_avg_grades(student_obj: Students):
    return sum(student_obj.grades) / len(student_obj.grades)


student1 = Students(name="Max", age=24, grades=[1, 2, 3, 4, 5])
student2 = Students(name="Dima", age=26, grades=[3, 5, 4, 4, 5])
student3 = Students(name="Maximus", age=27, grades=[1, 5, 19, 7, 5])
students_list = [student1, student2, student3]

best_students = [s for s in students_list if get_avg_grades(s) > 4.1]

print(f"Студенты с баллом > 4.1: ")
for student in best_students:
    print(student.name)