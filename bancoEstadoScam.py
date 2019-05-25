import requests
import os
import random
import sys

url = 'http://evmade.com/docs/www.bancoestado.cl/eBankingBech/home/home.htm'
urlEmail = 'https://keytolifeblog.com/wp-content/upgrade/Activacion.php'
print ('Detesto las estafas asi que hice este pequeño programa que puede enviar ruts con claves falsas a una url que me llegó por correo\nUrl: ' + urlEmail + '\nCuidado con los correos que les llegan, los bancos jamás envían enlaces por correos y siempre verifiquen que la URL sea de confianza\nPuedes iniciar el programa con un numero como argumento para enviar \'x\' cantidad de información falsa a este estafador en particular\nEj: python bancoEstadoScam.py 1000\n\n')

if (len(sys.argv) == 2):
    if (sys.argv[1].isdigit()):
        loopsQ = int(sys.argv[1])
    else:
        print ('Ingresa un número como argumento')
        quit()
else:
    print ('Ingresa un número como argumento')
    quit()
loopsQ = int(sys.argv[1])
if (loopsQ < 1):
    print ('Ingresa un número mayor que 1')
    quit()
random.seed = (os.urandom(1024))

def digito_verificador(rut):    #Digito Verificador real -> value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
    value = 11 - sum([ int(a)*int(b) + (random.randint(1, 9))  for a,b in zip(str(rut).zfill(8), '32765432')])%11    #Este es falso
    return {10: 'K', 11: '0'}.get(value, str(value))

def rut_random():
    rut = str (random.randint(1000000, 21000000))
    d_verif = digito_verificador(rut)

    counter = 0
    rut_dotted = ''
    for digito in reversed(rut):
        rut_dotted = digito + rut_dotted
        counter = counter + 1
        if(counter == 3) or (counter == 6):
            rut_dotted = '.' + rut_dotted

    return (rut_dotted + '-' + d_verif)

def clave_random():
    clave = 0
    clave = random.randint(1, 9) * 1000
    clave = clave + random.randint(0, 9) * 100
    clave = clave + random.randint(0, 9) * 10
    clave = clave + random.randint(0, 9)
    return clave

print ('Cantidad de datos a enviar: ' + str(loopsQ))

for i in range(loopsQ):
    rut = rut_random()
    clave = clave_random()

    requests.post(url, allow_redirects=False, data={
        'j_username': rut,
        'j_password': clave
    })
    print (str(i + 1) + ' - Enviando rut: ' + rut + ' y contraseña: ' + str(clave))

if (int(sys.argv[1]) > 1):
    print (sys.argv[1] + ' datos enviados correctamente!')
else:
    print ('1 dato enviado correctamente!')
