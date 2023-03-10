# 客户端，目标服务器为maya
import socket
import sys
BUFFER_SIZE = 4096

port = 20181

if len(sys.argv) > 1: # 如果针对此程序输入的参数大于1个那么port为第一个参数
    port = sys.argv[1] 

maya_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maya_socket.connect(("localhost", port)) # 两个括号是因为connect只接受一个元组

# maya_socket.sendall("cmds.file(new=True, force=True)".encode()) # python3中发送命令需要使用encode进行编码
# data = maya_socket.recv(BUFFER_SIZE) # 接受maya返回的值(字符串)
# print(data.decode())

# maya_socket.sendall("cmds.polySphere()".encode())
# data = maya_socket.recv(BUFFER_SIZE)
# result = eval(data.decode().replace('\x00','')) # 通过replace将空字符去除，然后通过eval将字符串转换成列表
# print(result[1])

maya_socket.sendall("def test():\n\tprint('Hello World')\ntest()".encode())
data = maya_socket.recv(BUFFER_SIZE)
print(data.decode())

maya_socket.close()
