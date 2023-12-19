# Script to download new certificate based on the certificate expiry date.

This script used Porkbun API to download the certificate. 
https://porkbun.com/api/json/v3/documentation#SSL%20Retrieve%20Bundle%20by%20Domain

1. Create an [API key](https://porkbun.com/account/api)
2. Put the files in this directory into the NGINX server.
3. Populate the .env file using API details.
4. Fill the other .env variables based on your setup.
5. Create a cron job so that it will check the certificate expiry and download the certificate.
