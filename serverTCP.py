import socket
import datetime
import sys
def preguntarPorNumeroClientes():
    while True:
        try:
            value = int(input('Escriba el número de clientes a esperar'))
        except ValueError:
            print('Tiene que ser un número menor o igual a 25')
            continue
        if value < 0 or value > 25:
            print('Tiene que ser un número positivo menor o igual a 25')
            continue
        else:
            break
    return value

def preguntarPorTamañoArchivo():
    while True:
        try:
            value = int(input('Escriba el tamaño del archivo para descargar (100 o 250)'))
        except ValueError:
            print('Tiene que ser 100 o 250')
            continue
        if value != 100 and value !=250:
            print('Tiene que ser 100 o 250')
            continue
        else:
            break
    return value

numeroClientes = preguntarPorNumeroClientes()
archivo = preguntarPorTamañoArchivo()

host = socket.gethostname()
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(3)

print ('Server listening on port ' + str(port) + '...')

try:
    clientesConectados = 0
    clientes = []
    ips=[]
    tiempo= []
    while clientesConectados < numeroClientes:
        s.bind('54.162.114.197', 8000)
        client, ip = s.accept()
        time = datetime.datetime.now()
        clientes.append(client)
        ips.append(ip)
        tiempo.append(time)
        print ('New connection from IP:', ip, 'Date/time:', time)
        client.send('OK'.encode())       
        confirmacion = s.recv(1024).decode()
        if(confirmacion == ('Listo para recibir el archivo')):
            print('Cliente detectado')
            clientesConectados+=1
        else:
            raise Exception('No se obtuvo confirmación del cliente')
        
except KeyboardInterrupt as e:
    print (e)
