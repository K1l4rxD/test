# test
You need to install the Docker-compose tool. The deployment of the web interface is done in an Ubuntu 20.04 container. Enter the following route to display the web interface: http://IP:3000. Use the docker-compose command to deploy the web interface: docker-compose up --build.

CONSIDER!!!

Edit the work.py file in the following section:

# MySQL Connection
app.config['MYSQL_HOST'] = '192.168.1.2'----->Enter the local IP
