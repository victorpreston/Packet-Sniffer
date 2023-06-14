# Network Packet Sniffer and Proxy Server

This project implements a network packet sniffer and a proxy server. The packet sniffer captures and analyzes network packets, extracting information from protocols such as HTTP, HTTPS, FTP, and DNS. The proxy server acts as an intermediary between clients and servers, allowing interception and decryption of HTTPS traffic.

## Features

- Network packet sniffing for HTTP, HTTPS, FTP, and DNS protocols.
- Decryption of HTTPS traffic using a custom SSL/TLS certificate.
- Logging and storage of captured packets and decrypted content.
- Proxy server functionality for intercepting and analyzing network traffic.
- Support for both plaintext and encrypted protocols.

## Prerequisites

- Python 3.7 or higher
- Dependencies listed in the `requirements.txt` file.

## Installation

1. Clone this repository to your local machine.


2. Navigate to the project directory.


3. Create a virtual environment (optional but recommended).


4. Activate the virtual environment.

- On Linux/macOS:
  ```
  source env/bin/activate
  ```
- On Windows:
  ```
  env\Scripts\activate
  ```

5. Install the required dependencies.


## Usage

1. Start the packet sniffer:


2. Start the proxy server:


3. Configure your device's network settings to use the proxy server.

4. Monitor the captured packets and decrypted content in the console output or log files.

5. Press `Ctrl + C` to stop the packet sniffer and proxy server.

## Configuration

- The `sniffer.py` file can be customized to extract and handle specific protocols or packet types.
- The `proxy_server.py` file can be configured to use a different SSL/TLS certificate or modify proxy behavior.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
