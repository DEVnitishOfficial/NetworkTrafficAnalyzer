import socket
import threading
import time
import random
import matplotlib.pyplot as plt

# Variables to store total received bytes
tcp_total_bytes = 0
udp_total_bytes = 0

# Lists to track bytes received per second
tcp_bytes_per_second = []
udp_bytes_per_second = []

# TCP Server
def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(1)
    print("TCP Server listening on port 5000...")
    conn, addr = server.accept()
    print(f"TCP Connection established with {addr}")

    while True:
        random_size = random.randint(100, 1000)  # Random packet size between 50 to 500 bytes
        message = b'a' * random_size
        conn.sendall(message)
        time.sleep(1)

# TCP Client
def tcp_client():
    global tcp_total_bytes
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print("TCP Client connected to server.")

    while True:
        data = client.recv(1024)
        if not data:
            break
        tcp_total_bytes += len(data)

# UDP Server
def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 6000))
    print("UDP Server listening on port 6000...")

    while True:
        random_size = random.randint(50, 500)  # Random packet size between 50 to 500 bytes
        message = b'b' * random_size
        server.sendto(message, ('localhost', 6001))
        time.sleep(1)

# UDP Client
def udp_client():
    global udp_total_bytes
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(('localhost', 6001))
    print("UDP Client ready to receive from server.")

    while True:
        data, addr = client.recvfrom(1024)
        if not data:
            break
        udp_total_bytes += len(data)

# Monitor and Plot function
def monitor_and_plot():
    global tcp_total_bytes, udp_total_bytes
    previous_tcp = 0
    previous_udp = 0

    duration = 20  # seconds
    for i in range(duration):
        time.sleep(1)
        # Calculate how much was received in the last second
        tcp_bytes = tcp_total_bytes - previous_tcp
        udp_bytes = udp_total_bytes - previous_udp

        tcp_bytes_per_second.append(tcp_bytes)
        udp_bytes_per_second.append(udp_bytes)

        previous_tcp = tcp_total_bytes
        previous_udp = udp_total_bytes

        print(f"Second {i+1}: TCP={tcp_bytes} bytes, UDP={udp_bytes} bytes")

    # Plotting
    seconds = list(range(1, duration + 1))
    plt.plot(seconds, tcp_bytes_per_second, label='TCP Bytes Received', marker='o')
    plt.plot(seconds, udp_bytes_per_second, label='UDP Bytes Received', marker='x')
    plt.title('Random Packets: Bytes Received per Second (TCP vs UDP)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Bytes Received')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
if __name__ == "__main__":
    threads = []
    threads.append(threading.Thread(target=tcp_server))
    threads.append(threading.Thread(target=tcp_client))
    threads.append(threading.Thread(target=udp_server))
    threads.append(threading.Thread(target=udp_client))
    threads.append(threading.Thread(target=monitor_and_plot))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
