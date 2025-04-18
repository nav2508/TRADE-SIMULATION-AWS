import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = "arn:aws:sns:us-east-1:961522281801:trade-alerts"  # Update this with your actual SNS ARN

    symbol = event.get("symbol", "UNKNOWN")
    value = event.get("value", 0)

    message = f" ALERT: {symbol} trade exceeded threshold! Value: ${value}"

    try:
        sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Trade Alert from Lambda"
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Alert sent via Lambda!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
