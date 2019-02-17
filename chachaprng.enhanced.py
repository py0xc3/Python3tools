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

from time import time
from time import sleep
from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class ChaChaPRNG(object):
    def __init__(self):
        a = str(time())
        b = str(time())
        c = str(time())
        nonce = bytes((a[len(a)-5:] + b[len(b)-5:] + c[len(c)-6:]), "UTF-8")
        key = urandom(32)
        sleep(0.1)
        key = key + urandom(32)
        prekey = bytes()
        for bits in range(0,32,1):
            stream = [key[bits] ^ key[(bits+32)]]
            prekey = prekey + bytes(stream)
            if bits == 31:
                key = prekey
        algorithm = algorithms.ChaCha20(key, nonce)
        cipher = Cipher(algorithm, mode=None, backend=default_backend())
        self.encryptor = cipher.encryptor()
    def getrand(self, length):
        value = str(time())
        random = self.encryptor.update(bytes(value[len(value)-length:], "UTF-8"))
        return random
