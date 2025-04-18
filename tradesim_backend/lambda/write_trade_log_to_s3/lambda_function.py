import json
import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket = "tradesim360-frontend"
    symbol = event.get("symbol", "AAPL")
    user_id = event.get("user_id", "unknown")
    trade_type = event.get("type", "BUY")
    value = event.get("value", 0)

    timestamp = datetime.datetime.utcnow().isoformat()
    data = {
        "timestamp": timestamp,
        "user_id": user_id,
        "symbol": symbol,
        "type": trade_type,
        "value": value
    }

    file_key = f"logs/{user_id}_{timestamp}.json"

    s3.put_object(
        Bucket=bucket,
        Key=file_key,
        Body=json.dumps(data),
        ContentType="application/json"
    )

    return {"statusCode": 200, "body": "Trade log saved to S3"}
