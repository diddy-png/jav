import socket
import protocol
from datetime import datetime
import random


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    if cmd == "TIME":
        response = protocol.create_msg(str(datetime.now().time())).encode()
    elif cmd == "NAME":
        response = (protocol.create_msg("zay_gezunt's_Server").encode())
    elif cmd == "RAND":
        response = (protocol.create_msg(str(random.randrange(1, 10))).encode())
    else:
        response = "out"
    return response


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            print(cmd)
            # 2. Check if the command is valid

            # 3. If valid command - create response
            if protocol.check_cmd(cmd):
                if create_server_rsp(cmd) == "out":
                    break
                client_socket.sendall(create_server_rsp(cmd))
            else:
                response = "Wrong command"
                print(f"problem is {response}")
        else:
            response = "Wrong protocol"
            # Attempt to empty the socket from possible garbage
            client_socket.recv(1024)
            print(f"problem is {response}")
        # Handle EXIT command, no need to respond to the client
        # Send response to the client

    print("Closing\n")
    # Close sockets\
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
