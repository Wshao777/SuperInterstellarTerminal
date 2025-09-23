import os
import argparse
import sys

# List of suspicious keywords that might indicate a backdoor or malicious code.
# This list can be expanded.
SUSPICIOUS_KEYWORDS = [
    # Common execution functions
    'eval(',
    'exec(',
    'subprocess.run',
    'subprocess.call',
    'subprocess.check_call',
    'subprocess.check_output',
    'os.system',
    'os.popen',

    # Obfuscation and encoding
    'base64.b64decode',
    'base64.b85decode',
    'marshal.loads',
    'pickle.loads',

    # Networking and remote connections
    'socket.socket',
    'urllib.request.urlopen',
    'requests.post',
    'requests.get',
    'nc -l -p', # Netcat listener
    'reverse_shell',

    # Keywords often found in web shells
    'php_uname',
    'passthru',
    'shell_exec',
    'proc_open',

    # Common crypto libraries that could be used for C2 communication
    'cryptography.fernet',

    # Direct references to sensitive files
    'id_rsa',
    '.ssh/authorized_keys'
]

# File extensions to scan. Add others if needed (e.g., '.php', '.js').
FILE_EXTENSIONS_TO_SCAN = ['.py', '.sh', '.rb', '.pl', '.js', '.php']

def scan_file(filepath):
    """Scans a single file for suspicious keywords."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for keyword in SUSPICIOUS_KEYWORDS:
                    if keyword in line:
                        print(f"\033[93m[!] Suspicious keyword '{keyword}' found in {filepath} on line {line_num}:\033[0m")
                        print(f"    {line.strip()}\n")
    except Exception as e:
        print(f"\033[91m[-] Error reading file {filepath}: {e}\033[0m")

def main():
    """Main function to parse arguments and start the scan."""
    parser = argparse.ArgumentParser(
        description="A simple backdoor scanner to find suspicious keywords in a directory.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("directory", help="The directory path to scan recursively.")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    scan_directory = args.directory

    if not os.path.isdir(scan_directory):
        print(f"\033[91m[-] Error: Directory not found at '{scan_directory}'\033[0m")
        return

    print(f"\n\033[94m[*] Starting scan in directory: {scan_directory}\033[0m")
    print("-" * 50)

    for root, _, files in os.walk(scan_directory):
        for file in files:
            if any(file.endswith(ext) for ext in FILE_EXTENSIONS_TO_SCAN):
                filepath = os.path.join(root, file)
                scan_file(filepath)

    print("-" * 50)
    print("\033[92m[+] Scan complete.\033[0m")
    print("Please review the findings above carefully. Not all findings may be malicious.")

if __name__ == "__main__":
    main()
