#!/usr/bin/env python3

import boto3
from prettytable import PrettyTable
import datetime
import os

# Create ./reports folder if not exists
if not os.path.exists("reports"):
    os.makedirs("reports")

def get_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                "InstanceId": instance['InstanceId'],
                "State": instance['State']['Name'],
                "Type": instance['InstanceType'],
                "AZ": instance['Placement']['AvailabilityZone']
            })
    return instances

def save_report(instances):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/ec2_report_{timestamp}.txt"

    table = PrettyTable(["Instance ID", "State", "Type", "Availability Zone"])
    for i in instances:
        table.add_row([i["InstanceId"], i["State"], i["Type"], i["AZ"]])

    with open(filename, "w") as f:
        f.write(str(table))

    print(f"\033[92m[✔] Report saved at {filename}\033[0m")

def main():
    print("\n🔎 Fetching EC2 instances...")
    instances = get_ec2_instances()
    if instances:
        save_report(instances)
    else:
        print("\033[91m[!] No EC2 instances found.\033[0m")

if __name__ == "__main__":
    main()
