import socket
import threading
from queue import Queue

# ====== Configuration ======
NUM_THREADS = 100
TIMEOUT = 1.0
results = []
port_queue = Queue()
lock = threading.Lock()

# ====== TCP Scan ======
def scan_tcp(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            return sock.connect_ex((ip, port)) == 0
    except:
        return False

# ====== Worker Thread ======
def worker(ip):
    while not port_queue.empty():
        port = port_queue.get()
        if scan_tcp(ip, port):
            with lock:
                results.append(port)
                print(f"✅ Port {port} is OPEN")
        port_queue.task_done()

# ====== Run Scanner ======
def run_scanner(ip, start_port=1, end_port=1024, output_file='open_ports.txt'):
    print(f"\n🔍 Scanning {ip} for open TCP ports ({start_port}-{end_port})...\n")

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(ip,))
        t.daemon = True
        t.start()

    port_queue.join()
    results.sort()

    # Save open ports to file
    with open(output_file, 'w') as f:
        for port in results:
            f.write(f"Port {port} is OPEN\n")

    print(f"\n✅ Scan complete! Open ports saved to '{output_file}'")

# ====== Main Entry Point ======
if __name__ == "__main__":
    print("=== Multi-threaded Port Scanner ===")
    target = input("Enter target IP or domain: ")

    try:
        target_ip = socket.gethostbyname(target)
        run_scanner(target_ip)
    except socket.gaierror:
        print("❌ Invalid IP or hostname.")
