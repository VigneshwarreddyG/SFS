# SFS-SERVICE FULLFILLMENT SYSTEM

## Overview
The Service Fulfillment System (SFS) is a versatile application designed to streamline service requests and management across various domains. With distinct services like car maintenance, grocery delivery, and accommodation bookings, SFS provides a seamless experience for customers, agents, and administrators.


# Environment setup

- Python 3.9.6
- Flask web framework
- MySQL database
- Docker

# Installation
- Clone the repository:git clone https://github.com/VigneshwarreddyG/sfs.git
- Creating a virtual environment
- Install dependencies:pip install -r requirements.txt
- Database configuration
- Apply database migrations

# Building and running the application
- Run the flask development server: flask run
- Access the application at http://localhost:5000
- Exploring the different services and functionalities via defiend endpoints
- Build the docker image: docker build -t sfs.app .
- Run the docker container: docker run -p 5000:5000 sfs-app




