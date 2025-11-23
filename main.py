import numpy as np

source = "МУЗЫКА_ОБЛАДАЕТ_МАГИЧЕСКОЙ_СИЛОЙ_-_ВДРУГ_СОБИРАЕТ_РАССЕЯННЫЕ_МЫСЛИ_И_ДАЕТ_ПОКОЙ_ВСТРЕВОЖЕННОЙ_ДУШЕ."
n = 11
m = 9

massive = np.array(list(source))
matrix = massive.reshape(m,n).T

res = ""
for i in range(n):
    for j in range(m):
        res += matrix[i][j]

print("Source: ", source)
print(f"Matrix: \n {matrix}")
print(f"Result: {res}")


