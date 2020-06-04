#!/bin/python3

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.x509 import load_pem_x509_certificate, ocsp
import base64

#OCSP
cert1 = open("pubkey.crt", "r")
authority1 = open("pubkey.crt", "r")
cert = cert1.read().encode()
authority = authority1.read().encode()

certloader = load_pem_x509_certificate(cert, default_backend())
authorityloader = load_pem_x509_certificate(authority, default_backend())
builder = ocsp.OCSPRequestBuilder()

builder = builder.add_certificate(certloader, authorityloader, SHA1())
prereq = builder.build()

request = base64.b64encode(prereq.public_bytes(serialization.Encoding.DER))

#Load the request:
ocsp_req = ocsp.load_der_ocsp_request(request)
#E.g. show serial
print(ocsp_req.serial_number)

#Response
ocsp_resp = ocsp.load_der_ocsp_response(request)
