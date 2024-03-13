import winrm
import argparse
import base64

def run_encoded_ps_script(ip, port, username, password, encoded_ps_script):

    decoded_ps_script = base64.b64decode(encoded_ps_script).decode('utf-16le')

    url = f'http://{ip}:{port}/wsman'

    session = winrm.Session(url, auth=(username, password), transport='ntlm')

    result = session.run_ps(decoded_ps_script)

    print("STDOUT:", result.std_out.decode())
    print("STDERR:", result.std_err.decode())

def main():
    parser = argparse.ArgumentParser(description="Run PowerShell script remotely using WinRM")
    parser.add_argument("-u", "--username", help="Username for authentication", required=True)
    parser.add_argument("-p", "--password", help="Password for authentication", required=True)
    parser.add_argument("-s", "--server", help="IP address of the remote server", required=True)
    parser.add_argument("--port", help="Port of the WinRM service default is 5985", default="5985")
    parser.add_argument("-x", "--script", help="PowerShell script to execute", required=True)

    args = parser.parse_args()

    run_encoded_ps_script(args.server, args.port, args.username, args.password, args.script)

if __name__ == "__main__":
    main()
