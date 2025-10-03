#!/usr/bin/env python3
"""
AWS Resource Tracker - EC2, S3, RDS
Tracks EC2 instances, S3 buckets, and RDS instances across all regions
"""

import boto3
from prettytable import PrettyTable
import botocore

def track_ec2():
    print("\n Tracking EC2 Instances...")
    regions = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]
    table = PrettyTable(["Region", "Instance ID", "Name", "Type", "State"])
    table.align = "l"

    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        try:
            reservations = ec2.describe_instances()['Reservations']
            for res in reservations:
                for inst in res['Instances']:
                    instance_id = inst['InstanceId']
                    instance_type = inst['InstanceType']
                    state = inst['State']['Name']
                    # Get Name tag if exists
                    name = ""
                    if "Tags" in inst:
                        for tag in inst['Tags']:
                            if tag['Key'] == 'Name':
                                name = tag['Value']
                    table.add_row([region, instance_id, name, instance_type, state])
        except botocore.exceptions.ClientError as e:
            print(f"Error fetching EC2 in {region}: {e}")

    print(table)

def track_s3():
    print("\n Tracking S3 Buckets...")
    s3 = boto3.client('s3')
    table = PrettyTable(["Bucket Name", "Creation Date", "Region"])
    table.align = "l"

    buckets = s3.list_buckets()['Buckets']
    for bucket in buckets:
        name = bucket['Name']
        creation_date = bucket['CreationDate'].strftime("%Y-%m-%d")
        try:
            region = s3.get_bucket_location(Bucket=name)['LocationConstraint']
            if not region:
                region = "us-east-1"  # default region
            table.add_row([name, creation_date, region])
        except botocore.exceptions.ClientError as e:
            table.add_row([name, creation_date, "Error fetching region"])

    print(table)

def track_rds():
    print("\n Tracking RDS Instances...")
    regions = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]
    table = PrettyTable(["Region", "DB Identifier", "Engine", "Status"])
    table.align = "l"

    for region in regions:
        rds = boto3.client('rds', region_name=region)
        try:
            instances = rds.describe_db_instances()['DBInstances']
            for db in instances:
                table.add_row([region, db['DBInstanceIdentifier'], db['Engine'], db['DBInstanceStatus']])
        except botocore.exceptions.ClientError:
            pass  # Region may not have RDS service enabled

    print(table)

if __name__ == "__main__":
    print("**** AWS Resource Tracker - EC2, S3, RDS ****")
    print("=" * 60)
    track_ec2()
    track_s3()
    track_rds()
    print("\n ## Tracking Completed. ##")
