
import boto3

resource = boto3.resource('ec2')
resource.create_instances(ImageId='ami-07d0cf3af28718ef8', InstanceType='t2.micro', KeyName='python', MaxCount=1, MinCount=1)