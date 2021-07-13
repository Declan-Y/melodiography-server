terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_s3_bucket" "b" {
  bucket = "melodiography-melodies"
  acl    = "private"

  tags = {
    Name        = "melodies"
    Environment = "Prod"
  }
}

resource "aws_s3_bucket" "c" {
  bucket = "melodiography-drawings"
  acl    = "private"

  tags = {
    Name        = "drawings"
    Environment = "Prod"
  }
}