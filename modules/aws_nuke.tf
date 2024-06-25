resource "aws_s3_bucket" "nuke_config_bucket" {
  bucket        = "atc-dce-aws-nuke-config"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "nuke_config_bucket_public_access_block" {
  bucket = aws_s3_bucket.nuke_config_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_object" "aws_nuke_config_object" {
  bucket = aws_s3_bucket.nuke_config_bucket.id
  key    = local.aws_nuke_config_object_key
  source = "fixtures/aws-nuke.yml"
  etag = filemd5("fixtures/aws-nuke.yml")
}

locals {
  aws_nuke_config_object_key = "config.yml"
}
