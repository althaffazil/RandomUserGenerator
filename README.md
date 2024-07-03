# Random User Generator

## Introduction

Random User Generator is a Flask application that generates random user data using a free API. The application is containerized with Docker and orchestrated using Docker Swarm for easy deployment.

## Features

- Generate random user profiles including name, email, address, etc.
- Easy setup and deployment using Docker and Docker Swarm
- Continuous Integration and Deployment using GitHub Actions

## Prerequisites

- Docker and Docker Compose installed

## Setup

### Local Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/althaffazil/random-user-generator.git
    cd random-user-generator
    ```

2. **Build the Docker image:**
    ```bash
    docker build -t cybervamp/random_user_generator-web:latest .
    ```

3. **Deploy the stack using Docker Swarm:**
    ```bash
    docker swarm init  # Run this only if Docker Swarm is not already initialized
    docker stack deploy -c docker-stack.yml random_user_generator
    ```

4. **Access the application:**
    Open your browser and navigate to `http://localhost:5000`.

