# 🔍 Multi-threaded Port Scanner (TCP)

A fast, efficient, and beginner-friendly **Python-based Port Scanner** built using `socket` and `threading`. This tool scans a target host for open TCP ports and saves the results to a file — ideal for learning networking, concurrency, and Python scripting.

---

## 📌 Features

- 🔄 Multi-threaded scanning for high-speed performance
- 🧠 Simple user input: enter an IP or domain
- ✅ Displays only open ports
- 🗂 Saves results to a text file
- ⏱ Adjustable thread count and timeout
- 💡 Beginner-friendly code with comments

---

## 📁 Project Structure

Port-Scanner/
├── main.py # Main scanner script
├── open_ports.txt # Output file for scan results (generated after run)
└── README.md # You're reading it!

---

## ⚙️ How It Works

1. The user enters a **target IP/domain name**
2. The script resolves the domain (if needed)
3. Ports from 1 to 1024 are added to a queue
4. `N` threads pull from the queue and scan each port using `socket`
5. Only **open** ports are printed and written to a file
6. The scanner stops once all ports are checked

---

## 🧠 Algorithm & Concepts

### 🧵 Threading:
- Python's `threading` module is used to create **concurrent port scanners**
- Each thread picks ports from a shared `Queue` and scans them independently

### 🛠 Socket Programming:
- Uses `socket.connect_ex()` to test TCP port status
- Open ports return `0`, closed ports return error codes

### 🔒 Thread Safety:
- A `Lock` is used to write results from multiple threads safely

---

## 🚀 How to Run

### Requirements:
- Python 3.x (no external libraries needed)

### Run via terminal or editor:
```bash
python main.py

**Example run:
=== Multi-threaded Port Scanner ===
Enter target IP or domain: scanme.nmap.org

🔍 Scanning scanme.nmap.org for open TCP ports (1-1024)...

✅ Port 22 is OPEN
✅ Port 80 is OPEN

✅ Scan complete! Open ports saved to 'open_ports.txt'

✨ Sample Output
Contents of open_ports.txt (example):
Port 22 is OPEN
Port 80 is OPEN


🧪 Test Targets
Try scanning these:
| Target            | Description                              |
| ----------------- | ---------------------------------------- |
| `scanme.nmap.org` | Public test server with known open ports |
| `127.0.0.1`       | Scan your own computer                   |
| `192.168.x.x`     | Scan local network devices               |


📌 To-Do / Future Features
 Add UDP scan support

 Allow custom port ranges

 Detect service banners

 Export results to CSV or JSON

 Scan multiple IPs or subnets

🧑‍💻 Built With
Python socket – network scanning

Python threading – concurrency

Python queue – thread-safe task distribution

📄 License
This project is open-source and free to use for educational and ethical purposes only. Please do not scan targets you do not own or have permission to test.

🙋‍♂️ Author
Aqib — https://github.com/AqibTayyab
Feel free to fork, star, or contribute! 💻✨



