data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "../src/"
  output_path = "../dist/daily-task-rotator.zip"
}

resource "aws_lambda_function" "daily_task_rotator" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "../dist/daily-task-rotator.zip"
  function_name = "notion-automator-daily-task-rotator"
  role          = aws_iam_role.daily_task_automator_role.arn
  handler       = "main.main"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.9"

  environment {
    variables = {
      DB_TASKS      = "bar"
      NOTION_SECRET = "foo"
    }
  }
}