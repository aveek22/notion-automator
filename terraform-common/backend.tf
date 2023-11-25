terraform {
  backend "s3" {
    bucket         = "terraform-remote-state-23gdc40"
    region         = "eu-west-1"
    encrypt        = "true"
    key            = "notion-automator/common-infra.tfstate"
    dynamodb_table = "terraform-statelock"
  }

  required_version = "1.5.7"

  required_providers {
    aws = {
      version = "5.24.0"
    }
  }
}
