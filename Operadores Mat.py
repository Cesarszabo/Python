from re import S


#print ('hello world')

a = int(input('entre com o primeiro valor: ')) # int para definir a classe do valor e input para receber o valor do usuario
b = int(input('entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print('soma: ' + str(soma))
# print('soma: {}' .format(soma))
# print('subtração: ' + str(subtracao))
# print('multiplicação: ' + str(multiplicacao))
# print('divisão: ' + str(divisao))
# print('resto: ' + str(resto))
# soma2 = a + 10
# print('soma2: {}' .format(soma2))

print('Soma: {So} \nSubtração: {sub} \nMultiplicação: {mul} \nDivisão: {div} \nResto: {r}' 
.format(sub = subtracao, So=soma, mul = multiplicacao, r = resto, div = divisao))



