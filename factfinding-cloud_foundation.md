# <p style="text-align: center;"><span style="font-family: Times New Roman; font-size: 3em;"> CLOUD FOUNDATION </span>

<p align="center"> <img src="https://cdn.dribbble.com/users/1912990/screenshots/6129020/media/5de7b1748ffb5977fc77840b16f939c5.gif" 
alt="drawing" width="800" height="600"/> </p>

# <p style= "text-align: center ; "> Cloud foundation 1 fact finding exercise. </span>
 
## <span style="color:#FF5733"> 1. What are IaaS, PaaS, and SaaS? </span>
 
- **IaaS (Infrastructure as a Service):** Provides virtualized computing resources over the internet. It includes virtual machines, storage, and networking components.
 
- **PaaS (Platform as a Service):** Offers a platform and environment for developers to build, deploy, and manage applications. It abstracts the underlying infrastructure.
 
- **SaaS (Software as a Service):** Delivers software applications over the internet on a subscription basis. Users can access the software via a web browser.
 
## <span style="color:#FF5733"> 2. What are the advantages of cloud computing? </span>
 
- **Scalability:** Easily scale resources up or down based on demand.
- **Cost-Efficiency:** Pay only for what you use, reducing upfront costs.
- **Flexibility:** Access resources from anywhere with an internet connection.
- **Reliability and Redundancy:** Cloud providers often have multiple data centers and backup systems.
- **Security:** Cloud providers invest heavily in security measures.
 
## <span style="color:#FF5733">3. What is an AWS Region? </span>
 
An AWS Region is a geographically separate area with multiple Availability Zones (data centers). Each Region is designed to be completely isolated from other Regions, allowing for fault tolerance and high availability.
 
## <span style="color:#FF5733"> 4. What is an Availability Zone? </span>
 
An Availability Zone (AZ) is a data center or cluster of data centers within an AWS Region. They are isolated from one another to ensure redundancy and minimize the risk of service disruption.
 
## <span style="color:#FF5733">  5. What are all the AWS Regions?  </span>

AWS has multiple Regions worldwide. Some examples include US East (N. Virginia), EU (Ireland), Asia Pacific (Tokyo), etc. Please refer to the official AWS documentation for the most up-to-date list.
 
##  <span style="color:#FF5733"> 6. What are the categories in which the AWS services are grouped?  </span>
 
AWS services are grouped into several categories, including Compute, Storage, Databases, Networking, Machine Learning, Analytics, Security, and more.

<p align="center"> <img src="https://docs.aws.amazon.com/images/connect/latest/adminguide/images/connect-overview2.png" alt="drawing" width="600" height="400"/> </p>
 
## <span style="color:#FF5733"> 7. What is the difference between object storage and block storage?   </span>
 
- **Object Storage:** Stores data as objects, each with a unique identifier. It's suitable for storing large amounts of unstructured data, like images, videos, and backups.
 
- **Block Storage:** Stores data in fixed-sized blocks and is typically used for structured data in file systems or databases.
 
## <span style="color:#FF5733"> 8. What are two AWS compute services, and what do these services do? </span>
 
- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. It allows users to run virtual servers, known as instances.
 
- **AWS Lambda:** A serverless computing service that lets you run code in response to events without the need to provision or manage servers.
 
## <span style="color:#FF5733"> 9. What are two AWS storage services, and what do these services do?  </span>
 
- **Amazon S3 (Simple Storage Service):** Object storage service for storing and retrieving any amount of data. It's highly scalable and designed for durability.
 
- **Amazon EBS (Elastic Block Store):** Provides block-level storage volumes that can be attached to EC2 instances. It's used for applications that require persistent, high-performance storage.

# <p style= "text-align: center ; "> Cloud foundation 2 fact finding exercise. </span> 

 <p align="center"> <img src="https://media.tenor.com/GO7C6FD0y3YAAAAC/aws.gif" alt="drawing" width="600" height="400"/> </p>

## <span style="color:#FF5733"> 1. What is the AWS shared responsibility model? </span> 
 
The AWS shared responsibility model defines the division of security responsibilities between AWS and the customer. AWS is responsible for the security of the cloud infrastructure, while the customer is responsible for securing their data in the cloud. This includes configuring security settings, managing access controls, and securing the content they upload to AWS services.
 
## <span style="color:#FF5733">2. What is an AWS Identity and Access Management (IAM) role? </span>
 
An IAM role is an AWS identity that allows AWS services to interact with other AWS resources securely. It is not associated with a specific user or group, but is assumed by authorized entities (e.g., EC2 instances, Lambda functions) to perform actions on your behalf. Roles are used to delegate permissions without having to share security credentials.
 
## <span style="color:#FF5733">3. What is an IAM policy? </span>
 
An IAM policy is a document that defines permissions and access rights. It is attached to AWS resources or IAM identities (users, groups, or roles). Policies are written in JSON format and specify what actions are allowed or denied on which AWS resources for which users or groups.
  
## <span style="color:#FF5733"> 4. What is an Amazon Machine Image (AMI)?  </span>
 
An Amazon Machine Image (AMI) is a pre-configured virtual machine image used to create EC2 instances. It contains the necessary information to launch an instance, including the operating system, application server, and any additional software. Users can choose from a variety of publicly available AMIs or create their own.
 
## <span style="color:#FF5733">5. What are the different Amazon EC2 instance types, and what are use cases for each type? </span>
 
Amazon EC2 offers a wide range of instance types optimized for different use cases:
 
- **General Purpose (e.g., t2, t3):** Balanced CPU, memory, and networking for a variety of workloads like web servers and small databases.
 
- **Compute Optimized (e.g., c5):** Ideal for compute-bound applications that benefit from high-performance processors.
 
- **Memory Optimized (e.g., r5):** Designed to deliver fast performance for workloads that process large data sets in memory.
 
- **Storage Optimized (e.g., i3):** Suited for workloads that require high, sequential read and write access to very large data sets.
 
## <span style="color:#FF5733">6. What is a virtual private cloud (VPC)? </span>
 
A Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account. It provides a logically isolated section of the AWS Cloud where you can launch resources like EC2 instances, RDS databases, and more. Users have complete control over their VPC, including selecting IP address ranges, creating subnets, and configuring route tables.
 
## <span style="color:#FF5733">7. What is the difference between a public and a private subnet? </span>
 
- **Public Subnet:** A subnet with a route to the internet via an Internet Gateway. Resources in a public subnet can have public IP addresses and can be reached from the internet.
 
- **Private Subnet:** A subnet without a direct route to the internet. Resources in a private subnet cannot be accessed from the internet by default. They can access the internet through a NAT Gateway or NAT instance if needed.

<p style="text-align: center;"><span style="font-family: Times New Roman; color:#FF5733"> Room 3 - Tanumatiben . Khalid . Hani . Moritala . Isra . Beewong </span>

<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/SNice.svg/640px-SNice.svg.png" width="200" height="200"/> </p>