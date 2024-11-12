grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_assessment = dict()

students1 = float(sum(grades[0]) / len(grades[0]))
students2 = float(sum(grades[1]) / len(grades[1]))
students3 = float(sum(grades[2]) / len(grades[2]))
students4 = float(sum(grades[3]) / len(grades[3]))
students5 = float(sum(grades[4]) / len(grades[4]))

sort_students = sorted(students) # Исправила имена переменных
student_assessment.update(({sort_students[0]: students1, sort_students[1]: students2, sort_students[2]: students3,
                            sort_students[3]: students4, sort_students[4]: students5}))
print(student_assessment)