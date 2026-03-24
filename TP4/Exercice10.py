#Exercice 10 : Prédire le résultat des programmes suivants : 
# Programme 1: l = 3 c = 4 L = [0] * l 
# print(L)
#  for i in range(l) : 
# L[i] = [0] * c 
# print(L)
#  Programme 2:
#  l = 3 c = 4
#  M = []
#  for i in range(l): 
# M.append([0] * c)
#  print(M) 
# Programme 3 :
#  l = 3 c = 4 
# a = [['1'] * c 
# for i in range(l)]
#  print(a)
#  Prédire le résultat : 
# L=[i 
# for i in range(1,20,2)] 
# print(L) M1=[j*2 
# for j in L] M2=[[j*2]
#  for j in L] M3=[[j]*2 
# for j in L]
#  print(“M1 : “,M1)
#  print(“M2:”,M2) 
# print(“M3:”,M3)

# Programme 1
l = 3
c = 4
L = [0] * l
print("Programme 1 - Étape 1:", L)  # [0, 0, 0]
for i in range(l):
    L[i] = [0] * c
print("Programme 1 - Étape 2:", L)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Programme 2
l = 3
c = 4
M = []
for i in range(l):
    M.append([0] * c)
print("Programme 2:", M)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Programme 3
l = 3
c = 4
a = [['1'] * c for i in range(l)]
print("Programme 3:", a)  # [['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1']]

L = [i for i in range(1, 20, 2)]
print("Liste L:", L)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


M1 = [j * 2 for j in L]
M2 = [[j * 2] for j in L]
M3 = [[j] * 2 for j in L]

print("M1 :", M1)   # [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
print("M2 :", M2)   # [[2], [6], [10], [14], [18], [22], [26], [30], [34], [38]]
print("M3 :", M3)   # [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19]]