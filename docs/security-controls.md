# Security Controls

## Encryption

- AWS KMS encrypts data stored in S3, DynamoDB, and Aurora.
- TLS 1.2+ protects all communications.
- Customer-managed KMS keys provide centralized key management.

## Identity and Access Management

- IAM roles follow least privilege principles.
- Amazon Cognito manages customer and employee identities.
- Multi-factor authentication is enforced.

## Monitoring and Auditing

- AWS CloudTrail records all API calls.
- Amazon CloudWatch provides monitoring and alerting.
- Logs support auditing and incident investigations.

## Data Protection

- S3 Versioning protects against accidental deletion.
- Lifecycle policies manage long-term retention.
- Access policies restrict unauthorized access.
