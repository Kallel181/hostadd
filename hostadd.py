#!/usr/bin/env python

import sys
import os

#This is a simple Script that adds or removes hosts from /etc/hosts


if ("-h" in sys.argv) or ("--help" in sys.argv):                                                            
    print("Usage: -a 127.0.0.1 hostname.com")
    print("       -r hostname.com")
    print("       -r 127.0.0.1")
    print()
    print("-a,    Adds a hosts to /etc/hosts")
    print("-r,    Removes a hosts to /etc/hosts")
    print("-s,    Show the content of /etc/hosts")

if "-s" in sys.argv:
    os.system("cat /etc/hosts")


if "-a" in sys.argv:
    if len(sys.argv) != 4:
        print("Invalid input")
    
    # ADD
    else:
        os.system("echo "+sys.argv[2]+" "+sys.argv[3]+"|sudo tee -a /etc/hosts")
        print("Host added")

if "-r" in sys.argv:
    if len(sys.argv) != 3:
        print("Invalid input")
    
    # REMOVE
    else:
        os.system("grep -v \""+sys.argv[2]+"\" /etc/hosts > /tmp/hosts1")
        os.system("sudo mv /tmp/hosts1 /etc/hosts")
        print("Host removed")
