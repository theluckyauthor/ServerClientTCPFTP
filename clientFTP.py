import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5000

s.connect((host, port))
print('Connected to socket '+host+':'+str(port))
a = b'Hello socket'
s.sendall(a)
print('Sending data to socket', a)
data = s.recv(1024)
print('Data received', repr(data))
# with open('test_file.txt', 'rU') as f:
    # data = f.read(1024)
    # print 'Sending file...',
    # s.send(data)
    # print 'OK'

s.close()