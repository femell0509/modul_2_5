def get_matrix(n, m, value):
    matrix = []
    for j in range(n):
         matrix.append([value]*m)
    return matrix
res_1 = get_matrix(2,2,10 )
res_2 = get_matrix(2,3,'x')
print(res_1)
print(res_2)
for i in res_1:
    print(*i)
for i in res_2:
    print(*i)
