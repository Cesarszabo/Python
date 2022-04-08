# for x in range(50, 101): #range considera a quantida contida no parenteses a partir do zero ou pode definir o inicio e o fim 
#     print (x)

# #  numeros primos de 0 a 100

# for num in range(101):
#     div = 0
#     for x in range(1,num+1):
#         resto = num % x
#         if resto ==0:
#             div +=1
#     if div == 2:
#         print(num)

# Calculo de media com validação do imput

a = int(input('Digite a nota do primeiro bimestre: '))
while a > 10:
    a = int(input('nota invalida digite novamente: '))
b = int(input('Digite a nota do segundo bimestre: '))
while b > 10:
    b = int(input('nota invalida digite novamente: '))
c = int(input('Digite a nota do terceiro bimestre: '))
while c > 10:
    c = int(input('nota invalida digite novamente: '))
d = int(input('Digite a nota do quarto bimestre: '))
while d > 10:
    d = int(input('nota invalida digite novamente: '))

media = (a+b+c+d)/4

print('sua media é: {}' .format(media))

