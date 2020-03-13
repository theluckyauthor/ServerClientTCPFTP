
import socket                   # Import socket module

newFile = ''
while True:
    selectedFile = input('Select a file size (100 or 250): ')
    if selectedFile == '100':
        newFile = './archivos/100.txt'
        break
    elif selectedFile == '250':
        newFile = './archivos/100.txt'
        break

pool = 0
while True:
    selectedPool = int(input('Select number of people to send the file (1): '))
    if selectedPool > 0:
        pool = selectedPool
        break

print('Pool of '+ str(pool)+ ' clients')
print('Selected File to transfer: '+newFile)
port = 8001                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostname()   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server: listening....')

poolCounter = 0
while True:
    
    conn, addr = s.accept()     # Establish connection with client.
    poolCounter = poolCounter+1
    print ('Server: Got connection from', addr)
    print ('Server: There are '+str(poolCounter)+ ' client(s) connected')
    print ('Server: You need '+str(pool)+' to send the file')
    if poolCounter == pool:
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

        print('Server: Done sending')
        # conn.send('Thank you for connecting'.encode())
        conn.close()
