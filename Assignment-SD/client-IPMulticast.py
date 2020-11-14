import socket
import time
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
for i in range(100000000000000):
    sock.sendto(str(i).encode(), (MCAST_GRP, MCAST_PORT))
    time.sleep(0.1)