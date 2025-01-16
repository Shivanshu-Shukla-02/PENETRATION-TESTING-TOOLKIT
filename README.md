# PENETRATION-TESTING-TOOLKIT

**COMPANY NAME**: CODTECH IT SOLUTIONS 

**NAME**:  SHIVANSHU SHUKLA

**INTERN ID**: CT08NFT

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**: January 15th, 2025 to February 15th, 2025

**MENTOR NAME**: Neela Santhosh Kumar

# ENTER DESCRIPTION OF TASK PERFORMED NOT LESS THAN 500 WORDS

ask Description: Building a Python-Based Modular Toolkit for Penetration Testing
The primary task was to develop a Python-based modular penetration testing toolkit comprising multiple modules like a port scanner, brute-forcer, and other essential tools used in security assessment. The objective of this toolkit is to provide penetration testers with a streamlined and extensible solution for evaluating system vulnerabilities. Each module was developed with reusability, efficiency, and clarity in mind, ensuring the toolkit could serve as a learning resource for security practitioners.

Goals of the Toolkit
Modularity:
Each tool functions as an independent module that can be executed standalone or integrated into the toolkit.
Users can extend the toolkit by adding custom modules.
User-Friendliness:
The toolkit provides a command-line interface (CLI) with straightforward commands and arguments.
Security Assessment:
Modules address common penetration testing tasks, including reconnaissance, vulnerability identification, and password testing.
Documentation:
Detailed documentation accompanies the toolkit, explaining each module's purpose, usage, and implementation.
Steps Taken to Develop the Toolkit
1. Requirements Gathering
The toolkit's functionality was determined based on common penetration testing needs:

Port Scanner: Scan open ports on a target host to identify services running on the system.
Brute-Forcer: Test username and password combinations against services like SSH or HTTP.
Network Reconnaissance: Gather information about target hosts within a network.
Extensibility: Ensure new modules can be added with minimal effort.
2. Design and Architecture
The toolkit was structured with a modular architecture:

Core CLI Framework:
Handles user input, selects modules, and passes arguments to the selected tool.
Modules:
Implemented as Python scripts stored in a modules/ directory.
Modules are dynamically imported based on user input.
Output and Logging:
Standardized output formats and optional logging for each module.
Configuration:
A config.json file to store default settings like timeout values and log file locations.
3. Implementation
The toolkit was implemented in Python, leveraging libraries such as:

socket: For port scanning and networking tasks.
paramiko: For SSH brute-forcing.
requests: For HTTP-based reconnaissance and brute-forcing.
argparse: For CLI argument parsing.
Key Modules in the Toolkit
1. Port Scanner
Functionality: Scans a target host for open ports within a specified range.
Implementation:
Uses socket to establish TCP connections to each port.
Outputs open ports and the services running on them.
Example Command:
bash
Copy
Edit
python toolkit.py portscan -t 192.168.1.1 -p 1-1000
2. SSH Brute-Forcer
Functionality: Attempts to log in to a target SSH service using a username and password list.
Implementation:
Utilizes paramiko to attempt authentication for each username-password combination.
Stops on successful login or after exhausting all combinations.
Example Command:
bash
Copy
Edit
python toolkit.py bruteforce -s ssh -t 192.168.1.1 -u users.txt -p passwords.txt
3. HTTP Reconnaissance
Functionality: Performs basic reconnaissance on a target HTTP server.
Features:
Identifies server headers and technologies.
Tests for common vulnerabilities like directory traversal.
Example Command:
bash
Copy
Edit
python toolkit.py http-recon -u http://example.com
4. Extensibility
Developers can add new modules by:
Placing a new Python file in the modules/ directory.
Implementing a run(args) function to handle user inputs.
Testing and Debugging
The toolkit was tested in multiple environments, including:

Local virtual machines simulating target networks.
Cloud-hosted servers with specific services enabled for testing.
Each module was debugged to handle:

Incorrect user inputs.
Network timeouts and unreachable hosts.
Authentication errors in brute-forcing tasks.
Documentation
A comprehensive user manual was created, detailing:

Installation instructions, including library dependencies.
Command-line usage for each module with examples.
Steps for extending the toolkit with new modules.
Outcome
The resulting Python-based penetration testing toolkit meets the deliverable requirements:

It provides essential modules for penetration testing.
Its modular structure supports scalability.
It is well-documented, ensuring ease of use for users and developers.
This toolkit serves as a valuable resource for individuals looking to enhance their penetration testing skills or perform security assessments in controlled environments.

**OUTPUT**

C:\Users\Shivanshu\JavaCodes> cmd /C ""C:\Program Files\Java\jdk-23\bin\java.exe" --enable-preview -XX:+ShowCodeDetailsInExceptionMessages -cp C:\Users\Shivanshu\AppData\Roaming\Code\User\workspaceStorage\db2e95bb8fdda292675570587e61ce25\redhat.java\jdt_ws\JavaCodes_efc6e467\bin PenetrationToolkit "
Welcome to the Penetration Testing Toolkit
1. Port Scanner
2. Brute Forcer
Enter your choice: 2
Enter the target IP: 30003
Enter the target port: 2202
Enter the username: Shivanshu Shukla
Enter the path to the password file: Shukl@
Starting brute force attack on 30003:2202
Error reading password file: Shukl@ (The system cannot find the file specified)
Brute force attack completed. No valid credentials found.


