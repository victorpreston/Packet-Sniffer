import socket
import dpkt

# Remote machine details
remote_ip = "192.168.1.100"  # Host IP 
remote_port = 12345  # Port number 

# Socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
sock.connect((remote_ip, remote_port))

# Port numbers
HTTP_PORT = 80
HTTPS_PORT = 443
FTP_PORT = 21
SMTP_PORT = 25

# Output file path
output_file = "captured_emails.txt"

# Open the output file in append mode
with open(output_file, "a") as file:
    # Sniff packets
    while True:
        packet = sock.recv(65535)
        eth = dpkt.ethernet.Ethernet(packet)

        # IPv4 packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)

            # TCP packets
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                src_port = tcp.sport
                dst_port = tcp.dport
                payload = tcp.data

                # Extract HTTP information
                if src_port == HTTP_PORT or dst_port == HTTP_PORT:
                    try:
                        http = dpkt.http.Request(payload)
                        method = http.method.decode()
                        uri = http.uri.decode()
                        host = http.headers.get("host", "").decode()

                        print("HTTP Request:")
                        print(f"Source IP: {src_ip}")
                        print(f"Destination IP: {dst_ip}")
                        print(f"Source Port: {src_port}")
                        print(f"Destination Port: {dst_port}")
                        print(f"Method: {method}")
                        print(f"URI: {uri}")
                        print(f"Host: {host}")
                        print()
                    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                        pass  # Not a valid HTTP packet

                # Extract FTP information
                if src_port == FTP_PORT or dst_port == FTP_PORT:
                    try:
                        print("FTP Packet:")
                        print(f"Source IP: {src_ip}")
                        print(f"Destination IP: {dst_ip}")
                        print(f"Source Port: {src_port}")
                        print(f"Destination Port: {dst_port}")
                        print()
                    except Exception as e:
                        print(f"Error handling FTP packet: {e}")

                # Extract SMTP information
                if src_port == SMTP_PORT or dst_port == SMTP_PORT:
                    try:
                        smtp = dpkt.smtp.SMTP(payload)
                        email = smtp.data.decode(errors="ignore")

                        # Write the email to the output file
                        file.write("Email:\n")
                        file.write(f"Source IP: {src_ip}\n")
                        file.write(f"Destination IP: {dst_ip}\n")
                        file.write(f"Source Port: {src_port}\n")
                        file.write(f"Destination Port: {dst_port}\n")
                        file.write("Content:\n")
                        file.write(email)
                        file.write("\n\n")
                    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                        pass  # Not a valid SMTP packet

