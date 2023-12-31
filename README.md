# SFS-SERVICE FULLFILLMENT SYSTEM

## Overview
The Service Fulfillment System (SFS) is a versatile application designed to streamline service requests and management across various domains. With distinct services like car maintenance, grocery delivery, and accommodation bookings, SFS provides a seamless experience for customers, agents, and administrators.


### Environment setup

- Python 3.9.6
- Flask web framework
- MySQL database
- Docker

### Installation
- Clone the repository:git clone https://github.com/VigneshwarreddyG/sfs.git
- Creating a virtual environment: python -m venv name_of_environment
- Install dependencies: pip install -r requirements.tx
- Database configuration: Replace your database uername and password in flask app
- Apply database migrations
- Installing Docker on your system
  
### Running the project via Docker
1) Install Docker on your system :https://www.docker.com/get-started/
2) Open PowerShell and execute the following commands:
docker pull charanl/sfs-image:latest
docker network create my-network
docker run -d --name mysql-container --network my-network -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=sfs mysql:latest
docker run -d --name php-container --network my-network -p 5000:5000 charanl/sfs-image:latest

### Building and running the application
- Run the flask development server: flask run
- Access the application at http://localhost:5000
- Exploring the different services and functionalities via defiend endpoints
- Build the docker image: docker build -t sfs.app .
- Run the docker container: docker run -p 5000:5000 sfs-app

### How to use flask for buliding the applications
Go through the below sites:
1)https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
2)https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/



