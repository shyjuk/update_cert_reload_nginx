from datetime import datetime
import OpenSSL
import ssl
import sys
import logging
from get_cert import main

from decouple import config

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT)

cert_path = config("CERTIFICATE_PATH")
renew_before = int(config("RENEW_BEFORE"))
cert = open(cert_path, "r").read()

x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
bytes=x509.get_notAfter()
#print(bytes)
timestamp = bytes.decode('utf-8')
#print (timestamp)

exp_date = datetime.strptime(timestamp, '%Y%m%d%H%M%SZ')
this_day = datetime.now()

days = (exp_date - this_day).days

if days < renew_before:
    main()
else:
    logging.info("Certificate is valid.")
