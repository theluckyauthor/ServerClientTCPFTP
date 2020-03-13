import socket                   # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = '54.162.114.197'  #Ip address that the TCPServer  is there
port = 8001                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send("Cliente: Hello server!".encode())

with open('received_file', 'wb') as f:
    print ('Cliente: file opened')
    while True:
        print('Cliente: receiving data from server')
        data = s.recv(1024)
        print('Servidor: data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Client: Successfully get the file')
s.close()
print('Client: connection closed')