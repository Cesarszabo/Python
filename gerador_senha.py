import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + '!@#$%¨&*()_+' #letras maiusculas e minusculas + numeros + caracteres especiais

rnd = random.SystemRandom() #gerador de numeros randômicos

print(''.join(rnd.choice(chars) for i in range(tamanho)))



