import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
    
for vpc in response["vpcs"]:
    print(vpc["vpcId"], vpc["CidrBlock"], vpc["IsDefault"])