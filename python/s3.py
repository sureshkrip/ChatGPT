import boto3
import zipfile
import io

def zip_s3_bucket_files(bucket_name, prefix, zip_file_name):
    # Create a session using your AWS credentials
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')

    zip_buffer = io.BytesIO()

    # Create a zip file in memory
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
        for obj in s3.Bucket(bucket_name).objects.filter(Prefix=prefix):
            # Download each file to local
            file_buffer = io.BytesIO()
            s3_client.download_fileobj(Bucket=bucket_name, Key=obj.key, Fileobj=file_buffer)
            file_buffer.seek(0)

            # Add file into zip file
            zip_file.writestr(obj.key, file_buffer.read())

    # Reset file pointer
    zip_buffer.seek(0)
    
    # Create a new object and upload the zip file
    s3.Object(bucket_name, f"{prefix}/{zip_file_name}").put(Body=zip_buffer)
    
bucket_name = "your_bucket_name" # replace with your bucket name
prefix = "your_directory" # replace with your directory in bucket
zip_file_name = "my_zip_file.zip" # replace with the name you want for your zip file

zip_s3_bucket_files(bucket_name, prefix, zip_file_name)












import awswrangler as wr

def read_csv_files(bucket, prefix):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)

    dfs = []
    for object in my_bucket.objects.filter(Prefix=prefix):
        if object.key.endswith('.csv'):  # ignore files that are not .csv
            df = wr.s3.read_csv(f's3://{bucket}/{object.key}')
            dfs.append(df)

    # Concatenate all dataframes into one
    all_data = pd.concat(dfs, ignore_index=True)
    
    return all_data

bucket = 'my-bucket'
prefix = 'my-directory/'

all_data = read_csv_files(bucket, prefix)
