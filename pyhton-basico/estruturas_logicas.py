#operadores relacionais
#igual a - ==
#diferente de - !=
#maior que - >
#menor que - <
#maior ou igual a - >=
#menor ou igual a - <=

#operadores lógicos
#and 
#or
#not

A = 5
B = 15
C = 20

print("A == B AND B > C : ", A == B and B > C)
print("A < B OR B > C : ", A < B or B > C)
print("NOT A == B : ", not A == B)


#estrutura de decisão/condicionais simples
#if
if (B > A):
  print(f'O numero {B} é maior que {A}')

#estrutura de decisão composta
#else

if (A > C):
  print(f'O numero {B} é maior que {A}')
else:
    print(f'O numero {C} é maior que {A}')

#if - elif - else
if (A > C):
  print(f'O numero {B} é maior que {A}')
elif (A > B):
    print(f'O numero {C} é maior que {A}')
else:
    print(f'O numero {C} é maior que {A}')

#estruturas de repetição
#for(para)
for n in range(10, -1, -1):
  print(n)

#while(enquanto)
x = 10
while x>=0:
  print(x)
  x=x-1