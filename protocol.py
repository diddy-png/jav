"""EX 2.6 protocol implementation
   Author:
   Date:
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol
        (e.g RAND, NAME, TIME, EXIT)"""
    if data in ('RAND', 'NAME', 'TIME', 'EXIT'):
        return True
    return False


def create_msg(data):
    """Create a valid protocol message, with length field"""
    return str(len(data)).zfill(2)+data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    len = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    if not len.isdigit():
        return False, "Error"
    return True, my_socket.recv(int(len)).decode()
