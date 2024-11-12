## Game Store App

  A game marketplace application that lets users browse and purchase games, similar to G2A. 
  The app features a Java-based frontend, a Python backend with CRUD capabilities, 
  and a SQLAlchemy database for storing game information. 
  This project is containerized with Docker and can be easily deployed using Docker Compose, Minikube, or 
  AWS resources set up via Terraform.

## Features

  Frontend: Built with Java to provide an interactive user interface resembling G2A.
  Backend: Python backend to handle CRUD operations on game data.
  Database: Uses SQLAlchemy to manage and store game-related data.
  Containerized: Configured to run in Docker containers for consistent deployment.
  Minikube Support: Set up to run on Minikube for local Kubernetes experimentation.
  AWS Ready: Terraform configuration files included to set up resources for running the app on AWS.
  Ease of Use: A setup.sh script is provided for streamlined setup and execution.

## Prerequisites

  Docker & Docker Compose: Required for containerization.
  Minikube: Needed to run on a local Kubernetes cluster.
  AWS CLI & Terraform: Required if deploying on AWS.
  Python and Java: Necessary for development.

## Installation

  Clone this repository:

  git clone https://github.com/SzekelyBoti/TerraDocker-Store.git
  cd TerraDocker-Store

  Run the setup.sh script to install dependencies and set up the project:

    ./setup.sh


  AWS Deployment (Terraform)

    Configure your AWS CLI with the required permissions.

    Use Terraform to provision AWS resources:

    terraform init
    terraform apply

    Once deployed, access the application via the AWS-provided endpoint.

## Usage

  Browse the game catalog, add games to your cart, and purchase games through the intuitive UI.