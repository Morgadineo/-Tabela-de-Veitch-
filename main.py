AB = []
C  = []
ABC = []

print("-- CONFIRA O CÓDIGO E A DESCRIÇÃO PARA ENTENDER --\n")
linhas = input(f"-Valores das linhas -\n")
colunas = input(f"--Valores das colunas\n")

AB = linhas.split(" ")
C  = colunas.split(" ")

m = len(AB)
n = len(C)

for i in range(m):
    ABC.append([])
    for j in range(n):
        ABC[i] = [0] * n

for i in range(m):
    for j in range(n):
        ABC[i][j] = AB[i] + C[j]

for i in ABC:
    print(i)
