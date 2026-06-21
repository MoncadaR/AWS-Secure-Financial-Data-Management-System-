# AWS Secure Financial Data Management System

## Overview

This project presents a secure, scalable, and compliant AWS architecture for a retail banking environment. The system is designed to support real-time access to customer profiles, transaction records, and financial documents while enforcing encryption, access control, monitoring, and compliance requirements.

## Business Problem

A retail bank with multiple branches and millions of customers needed to modernize fragmented customer data systems and outdated on-premise infrastructure. The goal was to improve data accessibility, scalability, security, and regulatory compliance using AWS cloud services.

## Objectives

- Enable real-time access to customer and transaction data
- Encrypt financial data at rest and in transit
- Support high availability and disaster recovery
- Scale during peak banking activity
- Align with PCI DSS, GLBA, and SOX compliance requirements

## AWS Services Used

- Amazon API Gateway
- AWS Lambda
- Amazon Cognito
- Amazon DynamoDB
- Amazon Aurora / RDS
- Amazon S3
- AWS KMS
- AWS Step Functions
- Amazon CloudWatch
- AWS CloudTrail

## Architecture

The architecture uses API Gateway as the secure entry point, Cognito for authentication, Lambda for transaction processing, DynamoDB and Aurora for data storage, S3 for document storage, KMS for encryption, and CloudTrail/CloudWatch for auditing and monitoring.

## Security Controls

- IAM least privilege access
- MFA using Amazon Cognito
- KMS encryption for S3, DynamoDB, and Aurora
- TLS 1.2+ for data in transit
- CloudTrail logging for API activity
- CloudWatch monitoring and alerting
- S3 Versioning and lifecycle policies

## Compliance Alignment

| Regulation | Security Implementation |
|---|---|
| PCI DSS | Encryption, tokenization, access control, audit logging |
| GLBA | Fine-grained access control and protection of customer financial data |
| SOX | Logging, versioning, monitoring, and record integrity controls |

## Scalability and Availability

- API Gateway and Lambda scale automatically with demand
- DynamoDB provides horizontal scalability
- S3 provides durable object storage
- Aurora Multi-AZ supports high availability
- Automated backups support recovery objectives

## Lessons Learned

This project strengthened my understanding of secure cloud architecture, compliance-driven design, IAM least privilege, encryption strategy, serverless scalability, and monitoring in regulated financial environments.
