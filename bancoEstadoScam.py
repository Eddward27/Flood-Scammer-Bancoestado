import requests
import os
import random
import sys

url = 'http://evmade.com/docs/www.bancoestado.cl/eBankingBech/home/home.htm'
print ('Detesto las estafas asi que hice este pequeño programa que puede enviar ruts con claves falsas a una url que me llegó por correo\nUrl: ' + url + '\nCuidado con los correos que les llegan, los bancos jamás envían enlaces por correos y siempre verifiquen que la URL sea de confianza\nPuedes iniciar el programa con un numero como argumento para enviar \'x\' cantidad de información falsa a este estafador en particular\nEj: python bancoEstadoScam.py 1000\n\n')

loopsQ = int(sys.argv[1])
random.seed = (os.urandom(1024))

def digito_verificador(rut):
    value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
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
    clave = random.randint(1, 10) * 1000
    clave = clave + random.randint(0, 10) * 100
    clave = clave + random.randint(0, 10) * 10
    clave = clave + random.randint(0, 10)
    return clave

for i in range(loopsQ):
    rut = rut_random()
    clave = clave_random()

    requests.post(url, allow_redirects=False, data={
        'j_username': rut,
        'j_password': clave
    })
    print ('Enviando rut: ' + rut + ' y contraseña: ' + str(clave))
