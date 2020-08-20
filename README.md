Python3tools
============


Useful Python 3 tools that proved to be helpful for some tasks, committed as deployed. 
Some will work standalone, some need to be integrated and adjusted. 
If not noted differently, they are tested under Fedora Linux and considered testing! 
Most tools are not maintained after committed! 
Do not use any tool in production environments without reviewing the code and its modules for contemporary issues. Be aware that the [security of some tools depends on the environment and fits only for particular purposes while being vulnerable in others](https://en.wikipedia.org/wiki/Side-channel_attack)! 
Review [issues](https://gitlab.com/py0xc3/Python3tools/issues) before deployment.     


``ChaChaPRNG``:

Based on https://github.com/pyca/cryptography

This CRNG was developed for Python 3.4 on CentOS 7.
``os.urandom`` does not offer high quality cryptographic random values before Linux 4.8, especially if much entropy has to be derived permanently.
Also, Python 3.4 does not contain the ``secrets`` module.

This tool is only intended for Linux operating systems before Linux 4.8 (then use ``os.random``), and for Python 3 before 3.6 (use ``secrets`` instead).

At this version, one derivation should not get more than 16 bytes at once. There is no limitation concerning the number of derivations.


``ChaChaPRNG enhanced``:

See ChaChaPRNG above.

Enhanced version that increases security through increased initial seed size and through a cryptographic entropy source that makes it harder to manipulate the entropy pool of the initial seed (e.g. when PRNG is used within virtual machines).

The enhanced version requires secrets module (Python 3.6+). Unlike a permanent use of the secrets module, this PRNG needs only on initialization an external entropy source (derived from secrets). After an object has been created, it is independent from external entropy. Appropriate for use in virtual machines if availability/quality of entropy is unknown.
If secrets cannot be provided (Python <3.6), use ChaChaPRNG above.


``PyCryFI``:

Based on https://github.com/pyca/cryptography

This is a small encryption/decryption tool for files. It needs Python 3.6 or later. Tested on Fedora 28.

It uses ChaCha20 with 256 bit. Blake2s is used for password hashing. The tool implements password salts.

The cryptographic security corresponds to 128 bit symmetric security, limited by hash collision probability of Blake2s, but sufficient for today. 

As soon as ``cryptography`` has implemented Blake2b with variable output length, I will upgrade the tool to 256 bit security.


``PyCryFI transitional 256``:

See ``PyCryFI``. This enhanced version uses Blake2b to reduce collision propability closer to 256 bit symmetric security. In order to reduce the key output to 256 bit (forced by ChaCha20) without variable output length, it uses XOR.

This is a temporary version that is to be replaced when Blake2b of ``cryptography`` supports variable output lengths. As the version is mature and the symmetric security is higher than 128 bit, it can be used in practice instead of PyCryFI (... while both versions are secure for today).


``Shaker``:

Using 'hashlib' and 'secrets' (should be part of most python3 installations).

Shaker widely resembles pycryfi.py but does not use ChaCha20 but SHAKE256 (variable-output function of SHA-3). Also, it does not use imported encryption/decryption functions like pycryfi.py but implements the encryption/decryption by itself. Only the algorithm itself is to be imported from "hashlib" (which should be part of nearly all python3 installations).

Shaker equals 256 bit symmetric security as long as the keystream (key stream == file size) is >64 byte.


``tviD``:

This improvised script shall manage Sundtek's MediaTV. Individual channels and frequencies can be added and selected using the console. It will start VLC with the choosen channel automatically. Automatic channel scanning is yet not implemented, channels have to be added manually to the script. 

If necessary, channel scanning as well as a GUI can be easily implemented using the doc of Sundtek in conjunction with ``os``, or ``subprocess`` modules.

It was developed/tested for Fedora Linux. The Sundtek driver for Linux has to be installed, also VLC Media Player.

The initial channels are working in Germany as of 20190129


``CTF_unsecure-encryption-tool``:

THIS IS A CAPTURE THE FLAG TASK TO ILLUSTRATE BAD USE OF CRYPTOGRAPHY - CTF_unsecure-encryption-tool IS NOT SECURE - DO NOT USE IT FOR PRODUCTION PURPOSES!  
  
A small beginner-level python3 capture the flag. It illustrates how data that was encrypted using secure cryptography (SHAKE256 from hashlib) can easily be stolen if the application developer did not know about how to use cryptographic functions. The application is vulnerable to a fundamental weakness of stream ciphers. To avoid misunderstandings, SHAKE256 is a secure Extendable Output Function and, if properly implemented into an application, can be used as a secure stream cipher (although there are better solutions like Salsa/ChaCha20 for stream cipher purposes, which are widespread and do not need to implement the (maybe vulnerable) stream functions separately). The weakness rises out of the misunderstanding, and therefore misuse, of a nonce in conjunction with a stream cipher implementation.  
  
"flagfile" is the encrypted flag that has to be decrypted.  
  
"CTF_unsecure-encryption-tool.py" is the unsecure tool that has to be hacked while "CTF_unsecure-encryption-tool.solution.py" includes a solution, implementing an attack that can recover the keystream in order to decrypt the flagfile without the key.

``ocsp-template.py``:

Based on https://github.com/pyca/cryptography

A template for [OCSP](https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol) that imports the OCSP implementation from ``cryptography``. This was developed and tested in January of 2019! Therefore, it is not tested against contemporary ``cryptography`` functions.  
  
The template assumes the certificate to be in a file ("pubkey.crt"). It can be adjusted to get the certificate directly using HTTP(S).

``getRootUsers.py``:

An ugly-scripted tool that identifies and lists all root-privileged accounts, and accounts that can potentially claim root-privileges under several circumstances. The tool considers /etc/passwd, /etc/shadow and /etc/group but not yet /etc/sudoers and /etc/sudoers.d/*. 
  
When an attacker obtained root-privileges, these files offer well opportunities to permanently establish root access, even if the initial attack vector was fixed.
