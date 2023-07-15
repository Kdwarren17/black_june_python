import boto3

s3 = client = boto3.client('s3')

response = s3.create_bucket(
    Bucket='warr-boto3-05012023'
    )
    
    print(response)
    
    

    
