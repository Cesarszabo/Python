import os #biblioteca os integra os recursos do Sistema Operacional

# ip_ou_host = input('Insira o IP ou host a ser verificado: ')

# os.system('ping -n 4 {} ' .format(ip_ou_host)) #Ping é o protocolo que testa a conexão com um site ou host


# def PingMultiplos():
#     arquivo = open('PingMultiplo.txt', 'r')
#     arquivo = arquivo.read

# print(PingMultiplos)

with open('PingMultiplo.txt') as file:
    dumb = file.read()
    dumb = dumb.splitlines()

for ip in dumb:
    print(ip)
    os.system('ping -n 2 {} ' .format(ip))
    print('#' * 60)
