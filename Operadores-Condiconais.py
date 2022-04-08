a = input('Primeiro valor: ')
b = input('Segundo valor: ')
c = input('Terceiro valor')

if a > b and a > c:
    print('o maior valor é: {}'.format(a))
elif b > a and b > c:
    print('o maior valor é: {}'.format(b))
else: 
    print('o maior valor é: {}'.format(c))