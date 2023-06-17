import boto3

def copy_folder(source_bucket, destination_bucket, source_folder):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(source_bucket)
    
    for obj in bucket.objects.filter(Prefix=source_folder):
        if obj.key.endswith('/'):  # Skip directories
            continue
        
        # Remove the source folder prefix from the object key
        destination_key = obj.key.replace(source_folder, '', 1)
        
        # Convert the destination folder to lowercase
        destination_key = destination_key.lower()
        
        # Copy the object to the destination bucket
        s3.Object(destination_bucket, destination_key).copy_from(
            CopySource={'Bucket': source_bucket, 'Key': obj.key}
        )

# Usage
source_bucket_name = 'your-source-bucket-name'
destination_bucket_name = 'your-destination-bucket-name'
source_folder_name = 'Your/Source/Folder/'

copy_folder(source_bucket_name, destination_bucket_name, source_folder_name)
