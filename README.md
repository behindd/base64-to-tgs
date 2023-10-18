# base64-to-tgs

Make sure you have the required tools (base64, kirbi2john, and sed) installed on your system for this script to work. You may also need to adjust the paths to these tools if they are not in your system's PATH.

Extracting Tickets from Memory with Mimikatz
mimikatz # base64 /out:true
mimikatz # kerberos::list /export

If we omit the base64 /out:true command in Mimikatz, it will extract the tickets and save them as .kirbi files. Depending on our network position and our ability to transfer files to our attack host, this method may simplify the process of cracking the tickets.

The bot takes the base64 blob retrieved above and prepares it for cracking. Copy and paste the base64 blob from the Mimikatz output and save it on a file.

This script first reads the base64 file, removes new lines and white spaces, decodes it into ticket.kirbi, runs kirbi2john to extract the hash, and then modifies it as specified before finally outputting "Ready for Hashcat! Please use mode 13100."
