import subprocess
import base64
import os

# Define ANSI color codes
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
RESET = "\033[0m"

# Define the ASCII art text
ascii_art = '''
  _       __ _  _     _          _______ _____  _____ 
 | |     / /| || |   | |        |__   __/ ____|/ ____|
 | |__  / /_| || |_  | |_ ___      | | | |  __| (___  
 | '_ \| '_ \__   _| | __/ _ \     | | | | |_ |\___ \ 
 | |_) | (_) | | |   | || (_) |    | | | |__| |____) |
 |_.__/ \___/  |_|    \__\___/     |_|  \_____|_____/ 
'''                                                      
                                                      

def main():
    print(f"{BLUE}{ascii_art}{RESET}")
    print(f"{RED}Name" f"{WHITE}:" f"{YELLOW} base64 to TGS{RESET}\n")
    print(f"{RED}☢"f"{YELLOW} Keep in mind this will overwrite your clipboard. Save your clipboard contents before proceeding!" f"{RED}☢{RESET}\n")
    b64_file = input("Enter the name of the base64 file: ")
    
    try:
        with open(b64_file, "rb") as file:
            base64_blob = file.read()
    except FileNotFoundError:
        print(f"{RED}File missing base64{RESET}")
        return

    print(f"{YELLOW}💀 Ticket prepared for Cracking:" f"{BLUE}tgs_hashcat{RESET}")

    # Remove new lines and white spaces from the base64 blob
    base64_blob = base64_blob.replace(b'\n', b'').replace(b' ', b'')

    # Decode the base64 blob and save it to 'ticket.kirbi'
    with open('ticket.kirbi', 'wb') as kirbi_file:
        kirbi_file.write(base64.b64decode(base64_blob))

    # Run 'kirbi2john' command to extract the hash and save the output to 'crack_file'
    with open('crack_file', 'w') as crack_file:
        subprocess.run(['kirbi2john', 'ticket.kirbi'], stdout=crack_file, text=True)

    # Modify the 'crack_file' as specified
    with open('crack_file', 'r') as crack_file:
        tgs_hashcat_lines = [
            f"$krb5tgs$23*{line.strip()}"
            for line in crack_file.readlines()
        ]
    
    with open('tgs_hashcat', 'w') as tgs_hashcat_file:
        tgs_hashcat_file.write('\n'.join(tgs_hashcat_lines))
    
    # Delete 'crack_file' and 'ticket.kirbi' files
    if os.path.exists('crack_file'):
        os.remove('crack_file')
    if os.path.exists('ticket.kirbi'):
        os.remove('ticket.kirbi')

    # Copy the contents of 'tgs_hashcat' to the clipboard using xclip
    subprocess.run(['xclip', '-selection', 'c', 'tgs_hashcat'])
    print(f"{GREEN}➜ Ready for Hashcat! Please use mode 13100{RESET}")
    print(f"{BLUE}➜ Contents of 'tgs_hashcat' copied to clipboard in case you plan \nto paste it on your local Windows machine for cracking.")

if __name__ == "__main__":
    main()
