#IMPORTS
import logging
import socket                   # Import socket module
import datetime
import hashlib
newFile = ''
#LOGGER
#Create and configure logger 
logging.basicConfig(filename="serverLogger"+ datetime.date.today().strftime("%B %d, %Y") + ".log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
#Creating an object 
logger=logging.getLogger()
#Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)

#INPUTS DE CONFIGURACIÓN
while True:
#2. Tener dos archivos disponibles para su envío a los clientes: un archivo de tamaño 100 MiB, y otro de 250 MiB. Se sugiera que uno de estos archivos sea multimedia.
#3. La aplicación debe permitir seleccionar qué archivo desea enviarse a los clientes conectados y a cuántos clientes en simultáneo. 
    selectedFile = input('Select a file size (100 or 250): ')
    if selectedFile == '100':
        newFile = './archivos/archivo1.txt'
        break
    elif selectedFile == '250':
        newFile = './archivos/archivo3.txt'
        break

pool = 0
while True:
    selectedPool = int(input('Select number of people to send the file (Max 25): '))
    if selectedPool > 0 and selectedPool < 26:
        pool = selectedPool
        break
    
print('Pool of '+ str(pool)+ ' clients')
print('Selected File to transfer: '+newFile)

#Calcular el Hash
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
hashCalculado = getmd5file(newFile)
print(hashCalculado)
#PROTOCOLO
#Creación del Socket: Puerto e IP
port = 8002                  # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostname()   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(selectedPool)                     # Now wait for client connection.

print ('Server: listening....')

poolCounter = 0
while True:
#1. Recibir conexiones TCP. La aplicación debe soportar 25 conexiones en simultáneo.     
    conn, addr = s.accept()     # Establish connection with client.
    poolCounter = poolCounter+1
    print ('Server: Got connection from', addr)
    print ('Server: There are '+str(poolCounter)+ ' client(s) connected')
    print ('Server: You need '+str(pool)+' to send the file')
    if poolCounter == pool:
#4. Realizar la transferencia de archivos a los clientes definidos en la prueba. 
#5. Definir el tamaño del buffer apropiado para su diseño. Realice diferentes pruebas para obtener el mejor desempeño en términos de tiempo de transmisión.
        data = conn.recv(1024)
        print('Server: received data from client,', repr(data))
        filename=newFile #In the same folder or path is this file running must the file you want to tranfser to be
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            print('Server: Sent ',repr(l))
            l = f.read(1024)
        f.close()
#4.5 Enviar el Hash
#6. La aplicación debe permitir medir el tiempo de transferencia de un archivo en segundos.         
#Al final de cada transferencia la aplicación debe reportar si el archivo está completo y
#correcto y el tiempo total de transferencia, para esto genere un log para cada intercambio de
#datos entre cliente y servidor. 
#7. Disponer un repositorio de los archivos recibidos y logs. (Revisar sección de recomendaciones).

        print('Server: Done sending')
        # conn.send('Thank you for connecting'.encode())
        conn.close()
