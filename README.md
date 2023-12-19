# Script to download new certificate based on the certificate expiry date.

This script uses [Porkbun API](https://porkbun.com/api/json/v3/documentation#SSL%20Retrieve%20Bundle%20by%20Domain) to download the certificate. 


1. Create an [API key](https://porkbun.com/account/api)
2. Put the files in this directory into the NGINX server.
3. Populate the .env file using API details.
4. Fill the other .env variables based on your setup.
5. Create a cron job so that it will check the certificate validity and download the certificate.
