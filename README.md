# hostadd
A simple script that adds or removes entries from /etc/hosts 

# Usage
Usage: 
-a 127.0.0.1 hostname.com

-r hostname.com

-r 127.0.0.1

----------------
-a,    Adds a hosts to /etc/hosts

-r,    Removes a hosts to /etc/hosts

-s,    Show the content of /etc/hosts

# Install 
```
chmod +x hostadd.py
mv hostadd.py hostadd
sudo cp hostadd /bin 
```

# Disclaimer
I made this piece of code for myself because i was tired of editing the /etc/hosts everytime i started a new machine in HTB, so, the code is usable, but not in any means good or optimal, it just works.
