import socket
import ssl

#dns_addr = "gemini.jaccident.co.uk"
#url = "gemini://" + dns_addr


def tls_handshake(connection, hostname) : 
    client_context = ssl.create_default_context()
    client_context.check_hostname = False
    client_context.verify_mode = ssl.CERT_NONE
    # I reckon here is where an evental TOFU implementation should be used.
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    ssock = client_context.wrap_socket(connection, server_hostname = hostname)
    return(ssock)


def gemini_request(addr) : 
    request = ("gemini://" + addr + "\r\n").encode('ascii')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock = tls_handshake(sock, addr)
    ssock.connect((addr, 1965))
    ssock.send(request)
    return(ssock)

def gemini_response(addr) : 
    ssock = gemini_request(addr)
    #read the whole message
    buff = ssock.recv(4096)
    message = None
    while (len(buff) > 0):
        if (message == None):
            message = buff
        else:
            message += buff
        buff = ssock.recv(4096)
    message = message.decode('utf-8')
    #This is where status code shenaniganery goes
    return(message)



#gemini_response()




