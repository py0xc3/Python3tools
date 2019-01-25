Python3tools
============

Some useful Python 3 tools, tested for Linux

General description
~~~~~~~~~~

These tools were developed to solve previously occurred problems, not yet solved by other tools/modules

ChaChaPRNG
~~~~~~~~~~

Based on https://github.com/pyca/cryptography

This CRNG was developed for Python 3.4 on CentOS 7.
``os.urandom`` does not offer high quality cryptographic random values before Linux 4.8, especially if much entropy has to be derived permanently.
Also, Python 3.4 does not contain the ``secrets`` module.

This tool is only intended for Linux operating systems before Linux 4.8 (then use ``os.random``), and for Python 3 before 3.6 (use ``secrets`` instead).

At this version, one derivation should not get more than 16 bytes at once. There is no limitation concerning the number of derivations.

PyCryFI
~~~~~~~~

Based on https://github.com/pyca/cryptography

This is a small encryption/decryption tool for files. It needs Python 3.6 or later.

It uses ChaCha20 with 256 bit. Blake2s is used for password hashing. The tool implements password salts.

The cryptographic security corresponds to 128 bit symmetric security, limited by Blake2s, but sufficient for today. 

As soon as ``cryptography`` has implemented Blake2b with variable output length, I will upgrade the tool to 256 bit security.
