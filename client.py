import socket
import protocol


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol.PORT))

    while True:
        user_input = input("Enter command\n")
        # Check if user entered a valid command as defined in protocol
        valid_cmd = protocol.check_cmd(user_input)

        if valid_cmd:
            # If the command is valid:
            # 1. Add length field ("RAND" -> "04RAND")
            # 2. Send it to the server
            my_socket.sendall(protocol.create_msg(user_input).encode())
            # 3. If command is EXIT, break from while loop
            if user_input == "EXIT":
                break
            # 4. Get server's response
            valid_msg, cmd = protocol.get_msg(my_socket)
            # 5. If server's response is valid, print it
            if valid_cmd:
                print(f"Server responded: {cmd}")
            else:
                print("Response not valid\n")
        else:
            print("Not a valid command")

    print("Closing\n")
    # Close socket
    my_socket.close()


if __name__ == "__main__":
    main()
