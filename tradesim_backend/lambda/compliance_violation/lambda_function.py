import json
import boto3

def lambda_handler(event, context):
    user_id = event.get("user_id")
    violation_type = event.get("violation", "Unknown Violation")

    message = f"Compliance Alert for User {user_id}: {violation_type}"

    sns = boto3.client('sns')
    topic_arn = "arn:aws:sns:us-east-1:961522281801:trade-alerts"

    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="Compliance Violation"
    )

    return {"statusCode": 200, "body": "Compliance violation triggered"}
