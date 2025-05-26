![Image](https://github.com/user-attachments/assets/61fd6afd-8fb0-4abe-ae92-bea9ff33c6a7)




# TradeSimulation - Cloud-Native Financial Trading Platform

## 1. Project Overview

**TradeSimulation** is a cloud-native, event-driven financial trading simulation platform developed as part of the **CSCI 5409** course. It enables users to simulate stock trading, monitor compliance, and receive real-time alerts without actual financial risk.

### Key Features:
- User registration & portfolio management  
- Rule-based compliance checks  
- Health monitoring & audit logging  
- Secure & scalable AWS deployment  

---

## 2. Objective

To design and deploy a **fully self-contained**, serverless, and infrastructure-as-code-driven simulation system that emulates a real-world trading environment. The focus is on modularity, scalability, service isolation, and secure operations.

---

## 3. Key Technologies Used

| Layer         | Technology                                                                 |
|---------------|----------------------------------------------------------------------------|
| Frontend      | ReactJS (Static site hosted on Amazon S3)                                 |
| Backend       | Flask (Python) on Amazon EC2 (private subnet)                             |
| Database      | PostgreSQL on Amazon RDS                                                  |
| Orchestration | AWS Lambda (alerts, compliance, logging, health checks)                   |
| Messaging     | Amazon SNS (email alerts)                                                 |
| Security      | IAM (LabRole), VPC subnet isolation, Security Groups                      |
| IaC           | AWS CloudFormation                                                        |
| Monitoring    | Amazon CloudWatch (EC2 & Lambda logs)                                     |

---

## 4. Architecture

**Figure 2: AWS Architecture Diagram**

The platform follows a hybrid cloud architecture leveraging both serverless and server-based components within a custom VPC:

- **Public Subnet**: API Gateway, S3-hosted frontend  
- **Private Subnet**: EC2 (Flask backend), RDS, and all Lambda functions  
- **S3 Bucket**: Stores static React frontend and audit logs  
- **API Gateway**: Secure API access layer  
- **Lambda**: Handles alerts, compliance, logging, and health checks  
- **SNS**: Email notifications for trade events  
- **CloudFormation**: Full-stack infrastructure provisioning  

---

## 5. Subnet Isolation & Security

Security is enforced via network architecture and IAM:

- **Custom VPC** with public/private subnets  
- **Private Subnet**: EC2 and RDS isolated from internet access  
- **Public Subnet**: Only API Gateway and S3 are exposed  
- **Security Groups**: Restrict EC2 and RDS communication  
- **IAM Roles**: All compute resources assume the pre-provided **LabRole**  

---

## 6. Deployment Flow

1. Provisionioned resources using **CloudFormation**
2. Deployed Flask backend to EC2 via Git
3. Built and uploaded React frontend to S3
4. Configured and deployed Lambda functions
5. Connected API Gateway to backend endpoints
6. Subscribed SNS for email-based trade alerts

---

## 7. Data Flow & Interactions

- Users access the React frontend on S3  
- Frontend communicates with API Gateway  
- API Gateway routes requests to EC2 or Lambda  
- EC2 interacts with RDS to persist user/trade data  
- Lambda functions handle compliance & monitoring  
- SNS sends real-time trade notifications  
- Logs are streamed to CloudWatch and optionally to S3  

---

## 8. Cost & Resource Estimation

The platform is optimized for **AWS Free Tier** use:

- EC2 (t2.micro) for backend  
- RDS (PostgreSQL free tier)  
- S3 (static frontend and logs)  
- Lambda, API Gateway, and SNS (within free quotas)  

> For full-scale use, consider costs for uptime, storage, notifications, and traffic.

---

## 9. Future Enhancements

- Add WebSocket support for real-time dashboard updates  
- Implement user authentication via Amazon Cognito  
- Set up CI/CD pipeline using AWS CodePipeline  
- Enable CloudTrail for advanced audit logging  
- Use AWS Step Functions for workflow orchestration  

---

## 10. Conclusion

**TradeSimulation** is a complete cloud-native platform demonstrating secure, modular, and event-driven architecture. It serves as a practical implementation for **CSCI 5409**, showcasing the use of AWS services to emulate real-world trading systems with a strong emphasis on performance, observability, and best DevOps practices.

---
