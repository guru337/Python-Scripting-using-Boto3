import boto3

response = client.get_bucket_acl(
    Bucket='guruprasad337123',
    ExpectedBucketOwner='string'
)
print(response)