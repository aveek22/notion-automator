data "aws_iam_policy_document" "daily_task_rotator_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

data "aws_iam_policy_document" "daily_task_automator_policy_document" {
  statement {
    effect    = "Allow"
    actions   = ["s3:*"]
    resources = ["*"]
  }
}

resource "aws_iam_role_policy" "daily_task_automator_role_policy" {
    name = "notion-automator-daily-task-automator-policy"
    role = aws_iam_role.daily_task_automator_role.id
    policy = data.aws_iam_policy_document.daily_task_automator_policy_document.json
}

resource "aws_iam_role" "daily_task_automator_role" {
  name               = "notion-automator-daily-task-automator-role"
  assume_role_policy = data.aws_iam_policy_document.daily_task_rotator_assume_role.json
}