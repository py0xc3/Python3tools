#!/bin/python3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from hashlib import shake_256
from getpass import getpass
from secrets import randbits
from secrets import token_hex

def enshakecry(data):
    nonce = bytes(token_hex(8), "UTF-8")
    salt = bytes(token_hex(8), "UTF-8")
    key = salt+bytes(getpass(), "UTF-8")
    rawstream = nonce + data
    size = int(len(rawstream))
    rawhash = shake_256(key)
    keystream = rawhash.digest(size)
    cryptedstream = bytes()
    for bits in range(0,size,1):
        cryptedstreambit = [rawstream[bits] ^ keystream[bits]]
        cryptedstream = cryptedstream + bytes(cryptedstreambit)
    marker = bytes(b"T5Fig4ZgkEWog846g543FqW2")
    print("stream cry: ", cryptedstream)
    return (marker+salt+nonce+cryptedstream)

def deshakecry(data, salt, nonce):
    key = salt+bytes(getpass(), "UTF-8")
    ### The following part is identical to "enshakecry" as there is no difference between encryption and decryption functions in stream ciphers
    ### The only difference is the nonce that was added in the beginning of the encryption process and has to be deleted at the end of the decryption process
    rawstream = data
    size = int(len(rawstream))
    rawhash = shake_256(key)
    keystream = rawhash.digest(size)
    cryptedstream = bytes()
    for bits in range(0,size,1):
        cryptedstreambit = [rawstream[bits] ^ keystream[bits]]
        cryptedstream = cryptedstream + bytes(cryptedstreambit)
    print("stream cry: ", cryptedstream[16:])
    return cryptedstream[16:]

print("Be aware that this program directly decrypts the given file on the hard drive and not on a temporary file system!")
print("If the file's directory, or the physical hard drive, is not protected from external access, you should copy/move it to a temporary file system before decrypting (mount -t tmpfs -o size=<size> none /PATH/TO/MOUNT/TMPFS)")
print("Enter the path including the file that has to be encrypted/decrypted! If there are more files, you can use tar (tar -cf <merged_file.tar> <file1> <file2>) to merge them. To quit the program, enter q")
print()

target = ""
file = ""

while 1:
    try:
        target = input()
        if target == "q":
            break
        with open(target, "b+r") as f:
            file = f.read()
        f.closed
        break
    except:
        print("File or path not existing, or cannot be accessed. Enter another /path/to/file or enter q for quit")
        print()

if target != "q":
    pycry = ""
    if file[:24] == bytes(b"T5Fig4ZgkEWog846g543FqW2"): #"\x8c\x14\xf6t\xea\xd5\xe3\x88Z\xa8~\xceE\x02w\\\xf4/w\xfa\xc6\xc5g}"):
        file = file[24:]
        salt = file[0:16]
        file = file[16:]
        nonce = file[0:16]
        file = file[16:]
        pycry = deshakecry(file, salt, nonce)
    else:
        pycry = enshakecry(file)

    if pycry != "":
        with open(target, "b+w") as f:
                file = f.write(pycry)
        f.closed
