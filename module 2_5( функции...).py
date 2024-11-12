# def get_matrix(n,m,value):
#     matrix=[]
#     for i in range(n):
#         matrix.append(n)
# list=[]
#         for j in range(m):
#             matrix.append(list_)value))
#     print(matrix)
# get_matrix(2,2,10)
# get_matrix(3,5,42)
# get_matrix(4,2,1)


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        empty = []
        matrix.append(empty)

        for j in range(m):
            empty.append(value)

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)