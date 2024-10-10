import boto3
import os

# Set environment variables for the credentials (optional but recommended)
os.environ['AWS_ACCESS_KEY_ID'] = 'APIWBQCCRVK3JK1QVTRK'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'MJIPcK5yyJ3YkZDCebkEU3okq9nwbyvYvSri69kG'

host = "https://gif.s3.iavgroup.local"
s3_client = boto3.client(
    's3',
    endpoint_url=host,
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    verify=r'C:\Downloads\IAV-CA-Bundle.crt'  # Set to the full path of your certificate
)

# Specify your bucket name
bucket_name = 'multi-modal-emotion-detection'

# Specify the local file path (adjust this to the correct path on your machine)
local_file_path = r'D:\Dataset\test.txt'  # Update this path to your actual file
normalized_file_path = os.path.abspath(local_file_path)  # Normalize the file path
print(f"Normalized file path: {normalized_file_path}")

file_name_in_s3 = 'Dataset/test.txt'  # Adjusted to include the file name

# Check if the local file exists and has the right permissions
if not os.path.isfile(normalized_file_path):
    raise FileNotFoundError(f"The local file {normalized_file_path} does not exist.")
if not os.access(normalized_file_path, os.R_OK):
    raise PermissionError(f"The local file {normalized_file_path} is not readable.")

# Read the content of the local file and upload it to S3
try:
    with open(normalized_file_path, 'rb') as file:  # Open the file in binary read mode
        s3_client.put_object(Body=file, Bucket=bucket_name, Key=file_name_in_s3)
    print(f"Uploaded {normalized_file_path} to {bucket_name}/{file_name_in_s3}")
except boto3.exceptions.S3UploadFailedError as e:
    print(f"Failed to upload {normalized_file_path} to {bucket_name}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
