import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    # Define the destination bucket and key
    destination_bucket = 'your-destination-bucket'
    destination_key = source_key  # You can modify this if needed
    
    try:
        # Download the file from the source bucket
        download_path = '/tmp/{}'.format(source_key)
        s3.download_file(source_bucket, source_key, download_path)
        
        # Upload the file to the destination bucket
        s3.upload_file(download_path, destination_bucket, destination_key)
        
        return {
            'statusCode': 200,
            'body': json.dumps('File transferred successfully!')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error transferring file')
        }