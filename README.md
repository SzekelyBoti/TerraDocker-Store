<a id="readme-top"></a>

<br />
<div align="center">
<h3 align="center">Game Store App</h3>

  <p align="center">
    A game marketplace application inspired by platforms like G2A. This app allows users to browse and purchase games, featuring a Java-based frontend, a Python backend with CRUD capabilities, and a SQLAlchemy-managed database. It is containerized with Docker and deployable via Docker Compose, Minikube, or AWS (using Terraform).
    <br />
    <a href="https://github.com/SzekelyBoti/TerraDocker-Store"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Game Store App is a modern game marketplace application with the following features:

    Frontend: Built with Java for an interactive user experience similar to G2A.
    Backend: Python-based backend for efficient CRUD operations.
    Database: SQLAlchemy for managing and storing game-related data.
    Containerization: Dockerized for consistent and portable deployments.
    Minikube Support: Runs locally on Kubernetes using Minikube.
    AWS Ready: Terraform scripts to deploy the app seamlessly on AWS.
    Ease of Use: A setup.sh script for streamlined installation and execution.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [![Java][Java]][Java-url]
* [![Python][Python]][Python-url]
* [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url]
* [![Docker][Docker]][Docker-url]
* [![Minikube][Minikube]][Minikube-url]
* [![Terraform][Terraform]][Terraform-url]
* [![AWS][AWS]][AWS-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

Ensure the following software is installed:

    Docker & Docker Compose
    Minikube
    AWS CLI & Terraform (for AWS deployment)
    Python & Java

### Installation

Clone the repo:

1. git clone https://github.com/SzekelyBoti/TerraDocker-Store.git
   cd TerraDocker-Store

2. Run the setup script:

  ./setup.sh

3. For AWS Deployment:

    Configure AWS CLI with required permissions.
    Deploy resources using Terraform:

    terraform init  
    terraform apply

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Browse the game catalog, add games to your cart, and purchase games through the intuitive UI. Once deployed:

    Access the app locally or via the AWS-provided endpoint.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add frontend for game catalog browsing
- [x] Implement CRUD operations
- [x] Containerize with Docker
- [x] Add Kubernetes support via Minikube
- [x] Provide Terraform scripts for AWS deployment

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Szekely Botond - [![LinkedIn][LinkedIn]][linkedin-url] - <szekelyboti1@gmail.com>

Project Link: [![GitHub][GitHub]][GitHub-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[GitHub]: https://img.shields.io/badge/GitHub-20232A?style=for-the-badge&logo=github&logoColor=61DAFB
[GitHub-url]: https://github.com/SzekelyBoti/TerraDocker-Store
[LinkedIn]: https://img.shields.io/badge/LinkedIn-20232A?style=for-the-badge&logo=linkedin&logoColor=61DAFB
[linkedin-url]: https://linkedin.com/in/boti-szekely
[Java]: https://img.shields.io/badge/Java-20232A?style=for-the-badge&logo=java&logoColor=61DAFB
[Java-url]: https://www.java.com/en/
[Python]: https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=61DAFB
[Python-url]: https://www.python.org/
[SQLAlchemy]: https://img.shields.io/badge/SQLAlchemy-20232A?style=for-the-badge&logo=sqlalchemy&logoColor=61DAFB
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[Docker]: https://img.shields.io/badge/Docker-20232A?style=for-the-badge&logo=docker&logoColor=61DAFB
[Docker-url]: https://www.docker.com/
[Minikube]: https://img.shields.io/badge/Minikube-20232A?style=for-the-badge&logo=minikube&logoColor=61DAFB
[Minikube-url]: https://minikube.sigs.k8s.io/docs/
[Terraform]: https://img.shields.io/badge/Terraform-20232A?style=for-the-badge&logo=terraform&logoColor=61DAFB
[Terraform-url]: https://www.terraform.io/
[AWS]: https://img.shields.io/badge/AWS-20232A?style=for-the-badge&logo=aws&logoColor=61DAFB
[AWS-url]: https://aws.amazon.com/