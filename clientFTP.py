import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8000

s.connect((host, port))
print('Conectado al socket '+host+':'+str(port))
#a = b'Hello socket'
#s.sendall(a)
#print('Sending data to socket', a)
# with open('test_file.txt', 'rU') as f:
    # data = f.read(1024)
    # print 'Sending file...',
    # s.send(data)
    # print 'OK'
data = s.recv(1024).decode()
if(data.equals('OK')):
    print('Servidor detectado')
else:
    raise Exception('No se obtuvo confirmación del servidor')
listo = 'Listo para recibir el archivo'
s.send(listo)
print('Enviado al servidor')

#Enviar archivo a clientes

s.close()