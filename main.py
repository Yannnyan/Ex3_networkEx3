# import socket module
from socket import *
import sys  # In order to terminate the program

FORMAT = "utf - 8"


# Prepare a sever socket
# Fill in start
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',8888))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    #Fill in end
    try:
        # Fill in start
        print('\n [RECV] receiving message . . .')
        message = connectionSocket.recv(1024)
        #Fill in end
        filename = message.split()[1]
        print("Opening File . . . ")
        f = open(filename[1:])
        print("Reading File . . . ")
        outputdata = f.read()
        print('[HTTP OK] sending HTTP OK')
        s = "HTTP OK"
        s = s.encode(FORMAT)
        connectionSocket.send(s)
        # Fill in start       #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        # Fill in end
        # Send the content of the requested file to the client
        print('[SEND] sending contents of files')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode(FORMAT))
        print('[CLOSE] closing connections')
        connectionSocket.close()
    except OSError:
        print("FAILED OPENING FILE DOESNT EXIST")
        connectionSocket.send("HTTP OK".encode(FORMAT))
        f = open("404eror.html")
        outputdata = f.read()
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode(FORMAT))
        connectionSocket.send("\r\n".encode(FORMAT))
        connectionSocket.close()

# Send response message for file not found
# Fill in start
# Fill in end
# Close client socket
# Fill in start
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data