# Compliance Mapping

| Requirement | AWS Control |
|------------|------------|
| Encryption at Rest | AWS KMS |
| Encryption in Transit | TLS 1.2+ |
| Access Control | IAM, Cognito, MFA |
| Audit Logging | CloudTrail |
| Monitoring | CloudWatch |
| Record Integrity | S3 Versioning |
| High Availability | Aurora Multi-AZ |
| Disaster Recovery | Backups and Versioning |

## Regulatory Alignment

### PCI DSS
- Encryption of sensitive financial data
- Strong authentication
- Logging and monitoring

### GLBA
- Protection of customer financial information
- Fine-grained access controls

### SOX
- Audit trails
- Data integrity
- Record retention
