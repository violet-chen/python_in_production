# 自定义服务器
import socket

BUFFER_SIZE = 4096
PORT = 21111


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    """ 
        创建一个socket别名为sock来负责监听
        with是一个语法糖 代表当代码离开with块的时候自动调用close方法来销毁这个
        socket.AF_INET代表使用的是IPv4的地址家族(address family)
        socket.SOCK_STREAM代表使用的是TCP协议 
    """
    sock.bind(("localhost", PORT)) # bind的功能是将创建的socket关联到主机的某一个网卡和端口上
    sock.listen() # 将socket置为监听状态并等待客户端的连接
 
    while True:

        connection, address = sock.accept() # 接受任意客户端的连接并返回一个新的socket以及客户端的IP地址
        # 这个socket主要负责与连接的客户端进行通信

        with connection:
            print("Connection Established: {0}".format(address))

            while True:
                data = connection.recv(BUFFER_SIZE) # recv(receive的缩写)方法接受客户端传来的信息，BUFFER_SIZE是一次性接受数据的最大长度，单位是字节   

                if not data:
                    break

                if data.decode().strip() == "stop":
                    connection.sendall(" Stopping server".encode())
                    connection.shutdown(1)
                    connection.close()
                    exit()

                connection.sendall(data)