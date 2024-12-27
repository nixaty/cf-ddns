import socket
import http.client


def check_internet_connection():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=5).close()
        return True
    except OSError:
        return False
    

def get_my_ipv4():
    try:
        addr_info = socket.getaddrinfo("ifconfig.me", 80, socket.AF_INET)
        if not addr_info:
            raise Exception("Can't get ipv4 address")

        ipv4_address = addr_info[0][4][0]

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipv4_address, 80))

        connection = http.client.HTTPConnection("ifconfig.me", 80, timeout=5)
        connection.sock = sock
        connection.request("GET", "/ip")

        response = connection.getresponse().read().decode()
        connection.close()
        return response
    except Exception as e:
        return f"ERROR: {e}"