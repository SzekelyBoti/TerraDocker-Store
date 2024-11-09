provider "aws" {
  region = "eu-north-1"
}
resource "aws_instance" "app_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  
  vpc_security_group_ids = [aws_security_group.app_security_group.id]
  
  tags = {
    Name = "MyAppServer"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras install docker -y
              service docker start
              usermod -a -G docker ec2-user
              sudo docker info
              curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose
              cd /home/ec2-user
              git clone https://github.com/SzekelyBoti/TerraDocker-Store.git
              cd TerraDocker-Store
              docker-compose up -d
              EOF
}
