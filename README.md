![Image](https://github.com/user-attachments/assets/61fd6afd-8fb0-4abe-ae92-bea9ff33c6a7)




1. Project Overview
TradeSimulation is a cloud-native, event-driven financial trading simulation platform developed as part of the CSCI 5409 course. The platform allows users to simulate stock trading, monitor compliance, and receive real-time alerts without actual financial risk. Key features include user registration, portfolio management, rule-based compliance checks, health monitoring, and logging—all built on a secure and scalable AWS architecture.

2. Objective
The goal was to design and deploy a fully self-contained serverless and infrastructure-as-code-driven simulation system that emulates a real-world trading environment. The architecture prioritizes modularity, scalability, and isolation of services for performance, security, and maintainability.

3. Key Technologies Used
Frontend: ReactJS static build hosted on Amazon S3

Backend: Flask application running on EC2 within a private subnet

Database: PostgreSQL hosted on Amazon RDS

Orchestration: AWS Lambda functions for trade alerts, compliance, logging, and health checks

Messaging: Amazon SNS for email alerts

Security: IAM roles (LabRole), VPC subnet isolation, Security Groups

Infrastructure-as-Code: AWS CloudFormation

Monitoring: Amazon CloudWatch for EC2 and Lambda logs

4. Architecture
Figure 2: AWS Architecture Diagram

The architecture comprises both serverless and server-based components arranged across public and private subnets within a single VPC. The following are key architectural highlights:

Public Subnet: Hosts the API Gateway and S3 frontend.

Private Subnet: Contains EC2 (Flask backend), RDS (PostgreSQL), and all Lambda functions.

S3 Bucket: Stores frontend React build (public read-only) and audit logs (restricted).

API Gateway: Routes API calls securely to the backend.

EC2 (Flask): Processes user registration, trades, and interacts with RDS.

Lambda Functions: Perform alerting, compliance checks, logging, and health monitoring.

SNS: Sends trade alerts to verified email addresses.

CloudFormation: Provisions all infrastructure including VPC, subnets, security groups, EC2, RDS, S3, Lambda, and SNS.

5. Subnet Isolation and Security
Security is enforced through careful network and identity configurations:

VPC Design: All resources are contained within a custom VPC.

Private Subnet: EC2 and RDS are inaccessible from the internet.

Public Subnet: Only S3 and API Gateway are exposed publicly.

Security Groups: EC2 and RDS communicate securely through controlled ports.

IAM: All Lambda functions and EC2 assume the pre-provided LabRole.

6. Deployment Flow
CloudFormation provisions all AWS resources.

Flask backend is deployed to EC2 using Git.

React frontend is built and uploaded to S3.

Lambda functions are created and mapped to events.

API Gateway is configured to route requests to backend.

SNS topic is subscribed for real-time notifications.

7. Data Flow and Interactions
Users interact with the S3-hosted frontend.

Frontend calls API Gateway which triggers backend logic via EC2 or Lambda.

EC2 interacts with RDS to persist user/trade data.

Lambda functions are triggered for compliance checks and alerts.

SNS sends email alerts for significant trade events.

Logs are streamed to CloudWatch and optionally saved to S3 as JSON.

8. Cost & Resource Estimation
The architecture is designed to operate within AWS Free Tier limits. Key components like Lambda, S3, and EC2 (t2.micro) are cost-optimized. A real-world deployment would incur costs primarily for:

EC2 uptime (if continuously running)

RDS instance and storage

S3 storage for frontend and logs

SNS notifications (beyond Free Tier)

9. Future Enhancements
Integrate WebSocket support for real-time dashboards.

Add Cognito for managed user authentication.

Add automated CI/CD pipeline using CodePipeline.

Introduce CloudTrail for deeper auditing.

Use Step Functions for multi-step workflows.

10. Conclusion
The TradeSimulation platform demonstrates an end-to-end cloud-native design that balances security, performance, and modularity. It leverages core AWS services in a hybrid delivery model and achieves full stack deployment via CloudFormation. This implementation meets the academic and technical requirements of CSCI 5409 while reflecting real-world best practices.
