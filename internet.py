import socket
import http.client


def check_internet_connection():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=5).close()
        return True
    except OSError:
        return False
    

def get_my_ipv4():
    connection = http.client.HTTPConnection("ifconfig.me")
    connection.request("GET", "/ip")
    return connection.getresponse().read().decode()