#!/usr/bin/python3

import hashlib
from getpass import getpass

print("What do you want to do?")
print("encrypt / hack")

action = input()
hasher = hashlib.shake_256()

if action == "encrypt":
    ###################key = bytes("YouWillNeverHackThisSecret!ImSure!!531", "UTF-8")
    k3y = getpass()
    key = bytes(k3y, "UTF-8")
    hasher.update(key)
    cipherstream = hasher.hexdigest(6)
    nonce = bytes("dL)2%q.Fs1O=", "UTF-8")
    ###################flag = bytes("Anoth3r-fl4g", "UTF-8")
    print("Enter the secret: ")
    flag = bytes(input(), "UTF-8")
    secret = nonce + flag
    cipherstream = cipherstream * 2
    ### If len() of flag would not be fixed, the following would possibly be a better approach:
    ### cipherstream = cipherstream * (int(len(secret)/len(cipherstream))+1)
    cipherstream = bytes(cipherstream, "UTF-8")
    l3n = 24
    ### If len() of flag would not be fixed, the following would possibly be a better approach:
    ### l3n = len(secret)
    crypted = bytes("", "UTF-8")
    for i in range(0,l3n,1):
        crypted = crypted + bytes([secret[i] ^ cipherstream[i]])
    cryptedfile = open("flagfile", "wb")
    cryptedfile.write(crypted)


if action == "hack":
    cryptedfile = open("flagfile", "rb")
    crypted = cryptedfile.read()
    nonce = bytes("dL)2%q.Fs1O=", "UTF-8")
    nonce = nonce + nonce
    l3n = len(crypted)
    cry = bytes("", "UTF-8")
    for i in range(0,l3n,1):
        cry = cry + bytes([crypted[i] ^ nonce[i]])
    cry0 = bytes("", "UTF-8")
    l3n = len(crypted)-12
    for i in range(0,l3n,1):
        cry0 = cry0 + bytes([cry[i] ^ crypted[i+12]])
    print(cry0)
