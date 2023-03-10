# 客户端，目标为自定义服务器
import socket
import sys

BUFFER_SIZE = 4096

port = 21111

if len(sys.argv) > 1:
    port = sys.argv[1]

maya_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maya_socket.connect(("localhost", port))

maya_socket.sendall("Echo Test".encode())
data = maya_socket.recv(BUFFER_SIZE)

maya_socket.close()