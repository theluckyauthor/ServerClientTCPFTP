#IMPORTS
import socket                   # Import socket module
import logging
import datetime
import hashlib
import os
import bufferTCP


#LOGGER
#Create and configure logger 
logging.basicConfig(filename="clientLogger"+ datetime.date.today().strftime("%B %d, %Y") + ".log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
#Creating an object 
logger=logging.getLogger()
#Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)

#PROTOCOLO
#Creación del Socket: Puerto e IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = '54.162.114.197'  #Ip address that the TCPServer  is there
port = 8004                  # Reserve a port for your service every new transfer wants a new port or you must wait.
# If server and client run in same local directory,
# need a separate place to store the uploads.
try:
    os.mkdir('downloads')
except FileExistsError:
    pass
#1. Conectarse al servidor TCP y mostrar que se ha realizado dicha conexión. Mostrar el estado de la conexión. 
s.connect((host, port))

#2. Enviar notificación de preparado para recibir datos de parte del servidor. 
s.send("Cliente: Hello server!".encode())
connbuf = bufferTCP.Buffer(s)
#3. Recibir un archivo del servidor por medio de una comunicación a través de sockets TCP.
#3.5 Recibir el Hash
while True:
        hash_type = connbuf.get_utf8()
        if not hash_type:
            break
        print('hash type: ', hash_type)

        file_name = connbuf.get_utf8()
        if not file_name:
            break
        file_name = os.path.join('uploads',file_name)
        print('file name: ', file_name)

        file_size = int(connbuf.get_utf8())
        print('file size: ', file_size )

        with open(file_name, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = connbuf.get_bytes(chunk_size)
                if not chunk: break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete.  Missing',remaining,'bytes.')
            else:
                print('File received successfully.')        
#4. Verificar la integridad del archivo con respeto a la información entregada por el servidor.
#Calcular el nuevo Hash
def getmd5file(archivo):
    try:
        hashmd5 = hashlib.md5()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashmd5.update(bloque)
        return hashmd5.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""
hashCalculado = getmd5file(f)
print(hashCalculado)
#5. Enviar notificación de recepción del archivo al servidor
#6. La aplicación debe permitir medir el tiempo de transferencia de un archivo en segundos.         
#Al final de cada transferencia la aplicación debe reportar si el archivo está completo y
#correcto y el tiempo total de transferencia, para esto genere un log para cada intercambio de
#datos entre cliente y servidor. 
#7. Disponer un repositorio de los archivos recibidos y logs. (Revisar sección de recomendaciones).

s.close()
print('Client: connection closed')