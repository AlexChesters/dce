resource "aws_iam_role" "api_admin_role" {
  name = "dce-api-admin-role"

  assume_role_policy = jsonencode({
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::637423502760:root"
        }
        Condition = {
          ArnLike = {
            "aws:PrincipalARN" = "arn:aws:iam::637423502760:role/aws-reserved/sso.amazonaws.com/*"
          }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "api_access_policy_attachment" {
  role = aws_iam_role.api_admin_role.name
  policy_arn = aws_iam_policy.api_execute_admin.arn
}
