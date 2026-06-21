import json
import boto3
import uuid
from datetime import datetime

from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
sfn = boto3.client("stepfunctions")
s3 = boto3.client("s3")

customer_table = dynamodb.Table("CustomerProfiles")
transaction_table = dynamodb.Table("TransactionRecords")

STEP_FUNCTION_ARN = "arn:aws:states:REGION:ACCOUNT_ID:stateMachine:BANK_WORKFLOW"
S3_BUCKET = "financial-documents-bucket"


def lambda_handler(event, context):
    try:
        action = event.get("action")
        customer_id = event.get("customerId", "CUST001")

        if action == "kyc":
            return start_kyc(customer_id)

        elif action == "transaction":
            return add_transaction(event, customer_id)

        elif action == "statement":
            return generate_statement(customer_id)

        else:
            return response(400, {
                "error": "Invalid action. Use kyc, transaction, or statement."
            })

    except Exception as e:
        return response(500, {"error": str(e)})


def start_kyc(customer_id):
    execution = sfn.start_execution(
        stateMachineArn=STEP_FUNCTION_ARN,
        input=json.dumps({
            "customerId": customer_id,
            "requestType": "KYC"
        })
    )

    return response(200, {
        "message": "KYC Step Function started",
        "executionArn": execution["executionArn"]
    })


def add_transaction(event, customer_id):
    transaction_id = str(uuid.uuid4())

    item = {
        "customerId": customer_id,
        "transactionId": transaction_id,
        "amount": event.get("amount"),
        "type": event.get("type"),
        "description": event.get("description", ""),
        "timestamp": datetime.utcnow().isoformat()
    }

    transaction_table.put_item(Item=item)

    return response(200, {
        "message": "Transaction added successfully",
        "transaction": item
    })


def generate_statement(customer_id):
    transaction_response = transaction_table.query(
        KeyConditionExpression=Key("customerId").eq(customer_id)
    )

    transactions = transaction_response.get("Items", [])

    statement_text = f"Statement for {customer_id}\n\n"

    for txn in transactions:
        statement_text += (
            f"{txn.get('timestamp')} | "
            f"{txn.get('type')} | "
            f"${txn.get('amount')} | "
            f"{txn.get('description')}\n"
        )

    file_key = f"statements/{customer_id}-{datetime.utcnow().date()}.txt"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=file_key,
        Body=statement_text,
        ContentType="text/plain"
    )

    return response(200, {
        "message": "Statement generated and saved to S3",
        "s3Bucket": S3_BUCKET,
        "s3Key": file_key
    })


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, default=str)
    }
