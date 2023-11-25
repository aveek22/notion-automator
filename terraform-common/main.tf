resource "aws_s3_bucket" "notion-automator-artifacts" {
  bucket = "notion-automator-artifacts"

  tags = {
    Name        = "notion-automator-artifacts"
    Environment = "production"
  }
}