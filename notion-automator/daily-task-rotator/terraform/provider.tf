terraform {
  backend "s3" {
    bucket  = "terraform-remote-state-23gdc40"
    key     = "terraform-state/daily-task-automator.tfstate"
    region  = "eu-west-1"
    encrypt = true
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-west-1"
}