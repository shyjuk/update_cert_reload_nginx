#!/usr/bin/env python3

import logging
import os
import sys
from decouple import config
import requests
import subprocess

# https://porkbun.com/api/json/v3/documentation
DEFAULT_API_URL = "https://porkbun.com/api/json/v3"
DEFAULT_CERTIFICATE_PATH = "/ssl/fullchain.pem"
DEFAULT_PRIVATE_KEY_PATH = "/ssl/privkey.pem"

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"


def main() -> None:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT)
    logging.info("Running SSL certificate renewal script")

    #print(config('DOMAIN'))

    domain = config("DOMAIN")
    api_key = config("API_KEY")
    secret_key = config("SECRET_KEY")

    logging.info("downloading SSL bundle for %s",  domain)
    #logging.info(domain)
    url = os.getenv("API_URL", DEFAULT_API_URL) + "/ssl/retrieve/" + domain
    r = requests.post(url, json={"apikey": api_key, "secretapikey": secret_key})

    data = r.json()
    #print (data)
    if data["status"] == "ERROR":
        logging.error(data["message"])
        sys.exit(1)

    certificate_path = config("CERTIFICATE_PATH", DEFAULT_CERTIFICATE_PATH)
    logging.info("saving certificate to %s", certificate_path)
    with open(certificate_path, "w") as f:
        f.write(data["certificatechain"])

    private_key_path = config("PRIVATE_KEY_PATH", DEFAULT_PRIVATE_KEY_PATH)
    logging.info("saving private key to %s", private_key_path)
    with open(private_key_path, "w") as f:
        f.write(data["privatekey"])
      
    logging.info("SSL certificate has been successfully renewed")
    logging.info("Reloading NGINX")
    status = subprocess.check_output("systemctl reload nginx",shell=True)


def getenv_or_exit(key: str) -> str:
    value = os.getenv(key)
    if value is not None:
        return value

    logging.error("%s is required but not set", key)
    sys.exit(1)


if __name__ == "__main__":
    main()      
