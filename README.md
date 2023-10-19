# base64-to-tgs

## Usage

- Copy the base64 blob (from Mimikatz) and save it on a file on your attacker machine.
- Run the script:

  ```bash
  python3 b64tgs.py
- Specify the file name.

Make sure you have the required tools (base64, kirbi2john, xclip, and sed) installed on your system for this script to work. You may also need to adjust the paths to these tools if they are not in your system's PATH.

Why use base64 to TGS? <br>

When the "base64 /out:true" command is not specified, Mimikatz will extract the tickets and save them as .kirbi files. Depending on our network position and our ability to transfer files to our attack host, this method may simplify the process of cracking the tickets.

Extracting Tickets from Memory with Mimikatz (Victim machine): <br>
- mimikatz # base64 /out:true <br>
- mimikatz # kerberos::list /export

The script takes the base64 blob retrieved above and prepares it for cracking. Copy and paste the base64 blob from the Mimikatz output and save it on a file.

This script first reads the base64 file, removes new lines and white spaces, decodes it into ticket.kirbi, runs kirbi2john to extract the hash, and then modifies it as specified to be able to use Hashcat against the hash before finally outputting "Ready for Hashcat! Please use mode 13100."

It also saves the contents of TGS file on your clipboard in case you plan to paste it on your local Windows machine for cracking. No need to open to copy the entire content! <br>

First, install xclip on your Linux if you haven't already: <br>
- sudo apt-get install xclip
