# AWS Resource Tracker

A simple Python-based tool to **track AWS resources** across all regions.
Currently supports **EC2 Instances, S3 Buckets, and RDS Instances**.

## Why Do We Need the AWS Resource Tracker
Companies shift to the cloud to avoid the heavy cost and effort of maintaining physical servers, data centers, and security patches, while benefiting from scalability and a pay-as-you-go model. However, even in the cloud, costs can quickly rise if resources are not tracked properly—for example, a developer may create an EC2 instance or S3 bucket for testing and forget to remove it, leading to continuous charges. This makes resource tracking essential to ensure efficiency and cost control.

---

## ✨ Features

* 🔍 **EC2 Tracking** – Lists all instances across regions with:

  * Instance ID
  * Name (tag)
  * Type
  * Current state

* 🪣 **S3 Tracking** – Lists all S3 buckets with:

  * Bucket name
  * Creation date
  * Region

* 🗄️ **RDS Tracking** – Lists all RDS instances across regions with:

  * DB Identifier
  * Engine type
  * Status

* 🌍 Multi-region support

* 📊 Outputs in **PrettyTable** format for better readability

---

## 📦 Requirements

* Python 3.7+
* AWS CLI configured with valid credentials (`aws configure`)
* Dependencies:

  ```bash
  python3 -m venv myvenv
  source myvenv/bin/activate
  pip install boto3 prettytable botocore
  ```

---

## ⚡ Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/aws-resource-tracker.git
   cd aws-resource-tracker
   ```

2. Run the script:

   ```bash
   python3 aws_resource_tracker_v1.py
   python3 aws_resource_tracker_v2.py

   ```

3. Example Output:

   ```
   **** AWS Resource Tracker - EC2, S3, RDS ****
   ============================================================
    Tracking EC2 Instances...
    +---------+-------------+---------+---------+--------+
    | Region  | Instance ID | Name    | Type    | State  |
    +---------+-------------+---------+---------+--------+
    | us-east-1 | i-0abcd123 | web-app | t2.micro | running |

    Tracking S3 Buckets...
    +-------------+--------------+-------------+
    | Bucket Name | Creation Date| Region      |
    +-------------+--------------+-------------+
    | my-bucket   | 2024-09-12   | us-east-1   |

    Tracking RDS Instances...
    +---------+----------------+---------+-----------+
    | Region  | DB Identifier  | Engine  | Status    |
    +---------+----------------+---------+-----------+
    | us-east-1 | mydb         | mysql   | available |
   ```

---

## 🔐 AWS Permissions

The script requires the following AWS IAM permissions:

* `ec2:DescribeInstances`
* `ec2:DescribeRegions`
* `s3:ListAllMyBuckets`
* `s3:GetBucketLocation`
* `rds:DescribeDBInstances`

Create a custom IAM policy with these permissions if running in a restricted environment.

---

## 📌 Notes

* `.terraform/` and state files are excluded from Git to keep repo lightweight.
* Default region for S3 buckets without explicit location is `us-east-1`.
* Errors for regions without RDS are ignored gracefully.

---

## 📜 License

MIT License – free to use and modify.

---
