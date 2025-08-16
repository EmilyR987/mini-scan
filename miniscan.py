import socket 

def port_scan(host, port):
    for port in port:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port)) 
            print(f"[+]Porta {port} aberta em {host}")   
        except:
            pass
        s.close()

port_scan("192.168.0.1" ,[21,22,80,443])
