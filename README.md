# Network-Port-Scanner

A network port scanner is a software tool used to discover open and closed ports on a networked device, such as a computer, server, or router. It's a fundamental tool for network administrators and security professionals to assess the security of a network and identify potential vulnerabilities.

Ports: In networking, a port is a virtual endpoint for communication. Ports are identified by numbers, and each number is associated with a specific service or application. For example, HTTP typically uses port 80, while HTTPS uses port 443.

Open vs. Closed Ports: Ports can be in one of three states: open, closed, or filtered. An open port means that a service or application is actively listening and can accept incoming connections. A closed port means that no service is listening on that port. A filtered port means that a firewall or security device is blocking access to the port.

Port Scanning: Port scanning is the process of systematically checking a range of ports on a target device to determine their status (open, closed, or filtered). This information can be used to identify running services and potential vulnerabilities.

Steps to Perform Network Port Scanning:
Identify the Target: Determine the target device or range of devices you want to scan. This could be a specific IP address, a subnet, or even an entire network.

Select a Port Scanner: Choose a suitable port scanning tool or software. There are both command-line and graphical user interface (GUI) tools available, such as Nmap, Masscan, and Angry IP Scanner.

Choose Scan Type: Decide on the type of scan you want to perform. The most common types of scans include:

TCP Connect Scan: Attempts to establish a full TCP connection with each port. It's slower but more reliable.
SYN/Stealth Scan: Sends SYN packets to target ports and analyzes the responses. Faster but less reliable.
UDP Scan: Scans for open UDP ports, which are commonly used for DNS, SNMP, and other services.
Custom Scans: You can customize scans based on specific needs and protocols.
Initiate the Scan: Run the chosen port scanner with the target IP address and port range. For example, to scan ports 1-100 on IP address 192.168.1.1 using Nmap.

Analyze Results: Examine the scan results to identify open ports and services running on the target device. The output typically includes information about the service, version, and other details.

Interpret Findings: Use the scan results to assess the security of the target. Open ports running unexpected services could indicate vulnerabilities. Closed ports may suggest a more secure configuration.

Take Action: Based on the findings, take appropriate actions to secure the network. This might involve closing unnecessary open ports, patching vulnerabilities, or configuring firewalls to block access to sensitive ports.

Document Findings: Maintain records of your port scanning activities, including the date, target, and results. Documentation is crucial for compliance and future reference.

Respect Legal and Ethical Considerations: Ensure that your port scanning activities comply with legal and ethical guidelines. Unauthorized or aggressive scanning can lead to legal consequences.

Remember that network port scanning should be conducted responsibly and with proper authorization. It's a valuable tool for both securing and assessing the security of networks, but it should be used with caution and in adherence to ethical standards and legal regulations.




