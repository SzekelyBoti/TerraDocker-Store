#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Starting project setup...${NC}"

echo "Choose an option:"
echo "1) Run locally with Docker Compose"
echo "2) Deploy to Minikube"
read -p "Enter choice [1 or 2]: " choice

if [ "$choice" == "1" ]; then
  echo -e "${GREEN}Running locally with Docker Compose...${NC}"
  docker-compose up --build

elif [ "$choice" == "2" ]; then
  echo -e "${GREEN}Deploying to Minikube...${NC}"
  
  minikube start

  kubectl apply -f minikube/backend-deployment.yaml
  kubectl apply -f minikube/backend-service.yaml
  kubectl apply -f minikube/frontend-deployment.yaml
  kubectl apply -f minikube/frontend-service.yaml

  echo -e "${GREEN}To access frontend:${NC} minikube service frontend-service"
  echo -e "${GREEN}To access backend:${NC} minikube service backend-service"
else
  echo -e "${RED}Invalid choice. Exiting setup.${NC}"
fi
