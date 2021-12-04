# import socket module
from socket import *
import sys  # In order to terminate the program

FORMAT = "utf - 8"


# Prepare a sever socket
# Fill in start
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',5050))
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
        print('[RECV] receiving message . . .')
        message = connectionSocket.recv(1024)
        print(f'Received message - {message}')
        #Fill in end
        filename = message.split()[1]
        if filename == b'/favicon.ico':
            print(f'Received message - /favicon.ico ')
            print('ignoring . . .\n')
        else:
            print(f"Opening File - {filename} . . . ")
            f = open(filename[1:])
            print("Reading File . . . ")
            outputdata = f.read()
            print('[HTTP OK] sending HTTP OK')
            connectionSocket.send("HTTP OK".encode())
            # Fill in start       #Fill in end
            # Send one HTTP header line into socket
            # Fill in start
            # Fill in end
            # Send the content of the requested file to the client
            print('[SEND] sending contents of files')
            connectionSocket.send(outputdata.encode())
            # for i in range(0, len(outputdata)):
            #     connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode(FORMAT))
            print('[CLOSE] closing connections\n')
        connectionSocket.close()
    except OSError:
            print("FAILED OPENING FILE DOESNT EXIST")
            connectionSocket.send("HTTP/1.1 200 OK")
            f = open("404eror.html")
            outputdata = f.read()
            connectionSocket.send(outputdata.encode())
            # for i in range(0, len(outputdata)):
            #     connectionSocket.send(outputdata[i].encode(FORMAT))
            connectionSocket.send("\r\n".encode(FORMAT))
            print("\n")
            connectionSocket.close()

# Send response message for file not found
# Fill in start
# Fill in end
# Close client socket
# Fill in start
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data