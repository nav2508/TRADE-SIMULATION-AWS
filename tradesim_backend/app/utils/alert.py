import boto3
import os

def send_alert(message):
    """
    Sends an alert message via SNS or prints locally if SNS is disabled.
    """
    try:
        topic_arn = os.getenv(
            "SNS_TOPIC_ARN",
            "arn:aws:sns:us-east-1:961522281801:trade-alerts"  # Updated ARN from screenshot
        )
        region = os.getenv("AWS_REGION", "us-east-1")

        sns = boto3.client("sns", region_name=region)
        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="TradeSim360 Alert"
        )
        return response
    except Exception as e:
        print(f"[LOCAL ALERT] {message}")
        print(f"[SNS ERROR] {str(e)}")
