import threading
import subprocess
import time

def start_proxy_server():
    # Start the proxy server
    subprocess.call(["python3", "proxy_server.py"])

def start_sniffer():
    # Start the sniffer
    subprocess.call(["python3", "sniffer.py"])

if __name__ == "__main__":
    # Start the proxy server in a separate thread
    proxy_thread = threading.Thread(target=start_proxy_server)
    proxy_thread.start()
    # Wait until proxy server is  running
    time.sleep(2)

    # Start the sniffer
    start_sniffer()
    proxy_thread.join()
