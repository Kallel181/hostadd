# hostadd
A simple script that adds or removes entryes from /etc/hosts 

# Usage
Usage: -a 127.0.0.1 hostname.com

       -r hostname.com
       
       -r 127.0.0.1

-a,    Adds a hosts to /etc/hosts

-r,    Removes a hosts to /etc/hosts

-s,    Show the content of /etc/hosts

# Install 
```
chmod +x hostadd.py
mv hostadd.py hostadd
sudo cp hostadd /bin 
```
