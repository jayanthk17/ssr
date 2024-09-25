import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2',
	aws_access_key_id = '',
	aws_secret_access_key = '',
	region_name = "ap-south-1"
	)
    
try:
    resource = ec2.start_instances(InstanceIds=[''], DryRun=False)
    print(resource)
except ClientError as e:
    print(e)
    

