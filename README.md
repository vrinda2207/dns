# DNS
A simple dns server 
Use the following commnands to run on ubuntu/linux
python3 simple_dns_server.py -o dns_server

Run the DNS Server (as root)
Since DNS uses port 53 (privileged port), you need to run it with sudo:
sudo ./dns_server

 Test the DNS Server
To test the DNS server, open a new terminal and use netcat (or nc), which is a simple networking utility.
For example, to resolve google. com, run the following:
echo -n "google.com" | nc -u -w1 localhost 5353

You should see an output of 142. 250.190.14, which is the IP address for google.com from the DNS server.
