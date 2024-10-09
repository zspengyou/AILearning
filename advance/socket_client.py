import socket

socket_client = socket.socket()

socket_client.connect("localhost",8888)

while True:
    msg = input("input your message: ")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8"))

    receive_data = socket_client.recv(1024)
    print(f"get message {receive_data.decode('utf-8')}")

socket_client.close()
      
