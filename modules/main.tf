terraform {
  # Tested up to 1.7.4
  required_version = ">= 0.13.7"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.26.0"
    }
  }

  backend "s3" {
    region = "eu-west-1"
    profile = "dce-master"
    bucket = "atc-terraform-backend-637423502760"
    key    = "dce/terraform.tfstate"
    dynamodb_table = "atc-terraform-backend"
  }
}

provider "aws" {
  region = var.aws_region
  profile = var.aws_profile
}

# Current AWS Account User
data "aws_caller_identity" "current" {
}

locals {
  account_id            = data.aws_caller_identity.current.account_id
  sns_encryption_key_id = "alias/aws/sns"
}
