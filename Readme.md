

# 🚀 Execution Flow (Step-by-Step)

1. **Start of Program (`__main__` section)**:
   - When you run the Python file, it **creates 5 threads**:
     - TCP Server
     - TCP Client
     - UDP Server
     - UDP Client
     - Monitor and Plot function

2. **Threads are started together**:
   - All 5 threads **start running simultaneously** (`thread.start()`).

---

# 🧩 Parallel Execution of Threads

### 1. TCP Server
- Listens on `localhost:5000` for TCP connection.
- Accepts connection from TCP Client.
- Every second:
  - Creates a **random-sized message** (50–500 bytes).
  - Sends it to TCP client.

### 2. TCP Client
- Connects to `localhost:5000` TCP Server.
- Listens for incoming TCP data.
- Whenever it receives data:
  - **Counts** how many bytes it received.
  - Adds to `tcp_total_bytes`.

---

### 3. UDP Server
- Binds to `localhost:6000` UDP port.
- Every second:
  - Creates a **random-sized message** (50–500 bytes).
  - Sends it to UDP Client (`localhost:6001`).

### 4. UDP Client
- Binds to `localhost:6001` UDP port.
- Listens for incoming UDP data.
- Whenever it receives data:
  - **Counts** how many bytes it received.
  - Adds to `udp_total_bytes`.

---

### 5. Monitor and Plot
- Waits for **1 second** ⏳
- After every second:
  - Calculates:
    - New TCP bytes received in this second.
    - New UDP bytes received in this second.
  - Saves these values into two lists:
    - `tcp_bytes_per_second`
    - `udp_bytes_per_second`
  - Prints in terminal:
    ```
    Second 1: TCP=240 bytes, UDP=150 bytes
    Second 2: TCP=300 bytes, UDP=200 bytes
    ```

- After 10 seconds:
  - **Stops monitoring**.
  - **Draws a graph**:
    - X-axis: Time in seconds (1,2,3,...10)
    - Y-axis: Bytes received
    - Two lines: TCP and UDP

---

# ✨ Visual Summary

```
TCP Server ➔ TCP Client ➔ Monitor Bytes ➔ Plot
UDP Server ➔ UDP Client ➔ Monitor Bytes ➔ Plot
All running at the same time!
```

---

# 🔥 Why Threads are Needed?
- **Servers and clients** must run at the same time (parallel).
- **Monitor** must watch them while they send/receive data.
- Python threads allow multiple "mini-programs" to run together.

---

# 🎯 Final Output
- Every second shows how many bytes received for TCP and UDP.
- At the end: a graph is plotted showing the trend!

---

# 🚦 Tiny Important Notes
- **TCP** is **connection-oriented**, so `server.accept()` is needed.
- **UDP** is **connectionless**, so just `sendto()` and `recvfrom()`.
- Random packet size creates a **real-world network traffic feel**.

---

# 🤔 In very simple words:
It’s like 2 shops (servers) are sending random gifts 🎁 every second to 2 customers (clients), and a camera 📸 (monitor) is recording how many gifts (bytes) they receive every second. After 10 seconds, the camera shows you a graph! 📈

---
