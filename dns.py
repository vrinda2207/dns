import socket
dns={"google.com": "142.250.190.78","example.com": "93.184.216.34","localhost": "127.0.0.1"}
HOST = "127.0.0.1"  # Listen on localhost
PORT = 5353   
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((HOST,PORT))
print(f"Custom DNS server running on {HOST}:{PORT}")
while True:
    data,address=server_socket.recvfrom(1024)
    domain=data.decode().strip()
    print(f"recieved query for {domain} from {address}")
    ip=dns.get(domain,"not found")
    server_socket.sendto(ip.encode(),address)
    print(f"responded with {ip}")
    
