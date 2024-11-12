grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johhny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_1 = []
list_1.append(sum(grades[0])/len(grades[0]))
list_1.append(sum(grades[1])/len(grades[1]))
list_1.append(sum(grades[2])/len(grades[2]))
list_1.append(sum(grades[3])/len(grades[3]))
list_1.append(sum(grades[4])/len(grades[4]))
print(list_1)

students = sorted (students)
print(students)
print(students[0],list_1[0],students[1],list_1[1],students[2],list_1[2],students[3],list_1[3],students[4],list_1[4],)