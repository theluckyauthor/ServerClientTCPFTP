import socket
import datetime

host = socket.gethostname()
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(3)

print ("Server listening on port " + str(port) + "...")

try:
    while True:
        client, ip = s.accept()
        time = datetime.datetime.now()
        print ('New connection from IP:', ip, 'Date/time:', time)
        data = client.recv(4096)
        text = 'you are connected to the socket ' + ip[0] + ':' + str(port) 
        client.send( text )
        # with file('test_file_server.txt', 'w+') as f:
            # f.write(data)
        client.close()
except KeyboardInterrupt as e:
    print (e)