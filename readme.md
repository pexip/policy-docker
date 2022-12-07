# **External policy server (Docker)**

This repo contains a "starter" external policy server, utilizing Python, django and gunicorn.  This deployment guide assumes some knowledge of docker.  When deployed, it will build and run four docker containers:

- **policy:** Python container running django/gunicorn
- **nginx:** reverse proxy fronting policy and serving TLS
- **certbot:** gets LetsEncrypt certs for server
- **cron:** checks daily if certs need to be renewed

---

### **Deployment**


1. Create a virtual machine using the OS of your choosing.  In order to use the LetsEncrypt certs, this VM should have a public IP.
2. Open ports 80/443 to your VM in the firewall.
3. Create a DNS record (either A or CNAME) for your policy server pointing to your VM.
4. Install docker and docker compose on your VM.
5. Clone this repo onto your VM.
6. Modify config.env with your own information:
    - **HOSTNAME:** FQDN of your VM, matching the DNS record created above.
    - **CERTBOT_EMAIL:** Your email address, to be notified of possible cert expiration.
    - **CERTBOT_TEST_CERT:** 0 for production cert, 1 for staging cert.  Use a staging cert for testing as this does not rate limit requests.  However, the staging cert will not be trusted.
    - **CERTBOT_RSA_KEY_SIZE:** Change if you wish to change from the default value of 4096.
7. Create the permanent volume for storage of certificates by running `docker volume create --name=certs`
8. In the root folder of the repo, run
    `docker compose up -d`
9. On the first run, it will take some time for the certs to be obtained and installed.  You can check the running containers with `docker ps`

---

### **Usage**


Policy functions are in the Python file `policy.py`.  This file is by default in the root directory of the repo, and mapped into the docker image.  If you wish to place this file in a different local location, modify the highlighted portion of this line in `docker-compose.yaml`:

<pre>
      - <b>./policy.py</b>:/app/server/policy.py
</pre>

`policy.py` must contain these functions (not all need be used in Pexip policy):

- `service_config` - Service configuration policy
- `location` - Media location policy
- `avatar` - Participant avatar policy
- `reg` - Registration alias policy

If additional modules are necessary, add them to `policy/requirements.txt`, delete your current docker container and image, and create a new one with `docker compose up -d`.