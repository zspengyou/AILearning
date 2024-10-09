import socket
# create socket
socket_server = socket.socket()
# bind ip and port
socket_server.bind(("localhost", 8888))
# listen
socket_server.listen(1)
# wait for client
while True:
    conn, address = socket_server.accept() # conn is object, address is client side address info
    print(f"receive client side info: {address}")

    data:str = conn.recv(__bufsize=1024).decode("UTF-9")
    print(f"data from client is {data}")
    msg = input("please input your message ")
    if(msg == "exit"):
        break
    conn.send(msg.encode("UTF-8"))
conn.close()
socket_server.close()



