import hashlib

texto = input('Digite o texto a ser gerado a Hash: ')

code = int(input(''' ##### Menu - Escolha o tipo de Hash #####
                    1 - MD5
                    2 - SHA1
                    3 - SHA256
                    4 - SHA512
                    Digite o numero do tipo de Hash a ser gerado '''))

if code == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print('A hash MD5 do texto : ', texto, 'é: ', resultado.hexdigest())
elif code == 2: 
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print('A hash SHA1 do texto : ', texto, 'é: ', resultado.hexdigest())
elif code == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print('A hash SHA256 do texto : ', texto, 'é: ', resultado.hexdigest())
elif code == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print('A hash SHA512 do texto : ', texto, 'é: ', resultado.hexdigest())
else: 
    print('Seleção feita fora das opções do menu')



