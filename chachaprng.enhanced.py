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
from cryptography.hazmat.primitives import hashes

class ChaChaPRNG(object):
    def __init__(self):
        nonce = bytes(token_hex(8), "utf-8")
        key = bytes(token_hex(32), "utf-8")
        hasher = hashes.Hash(hashes.BLAKE2b(64), backend=default_backend())
        hasher.update(key)
        key = hasher.finalize()
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
        random = ""
        while len(random) != length:
            value = str(time())+token_hex(22)+str(time())
            random = self.encryptor.update(bytes(value[len(value)-length:], "UTF-8"))
        return random
