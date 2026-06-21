# Data Flow

## Customer Request

A customer accesses the banking application and submits a secure HTTPS request through Amazon API Gateway.

## Authentication

Amazon Cognito validates user credentials and enforces multi-factor authentication.

## Processing

AWS Lambda processes requests and applies business logic such as transaction validation and fraud checks.

## Workflow Coordination

AWS Step Functions orchestrates workflows such as account updates, KYC verification, and loan processing.

## Data Access

- Amazon DynamoDB stores customer profiles and transaction records.
- Amazon Aurora stores relational banking information.
- Amazon S3 stores documents such as statements and reports.

## Monitoring

AWS CloudTrail records API activity and AWS CloudWatch monitors performance and operational events.

## Response

The processed response is returned securely to the banking application using HTTPS and JSON.
