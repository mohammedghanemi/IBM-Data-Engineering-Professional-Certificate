import boto3
import os
# Set environment variables for the credentials (optional but recommended)
s3_client = boto3.client('s3')
os.environ['AWS_ACCESS_KEY_ID'] = 'APIWBQCCRVK3JK1QVTRK'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'iBIGpCoupBmk8glBKOrCb5CiIELLvl5K'
host = "https://gif.s3.iavgroup.local"
s3_client = boto3.client(
    's3',
    endpoint_url=host,
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    verify=r'C:/Users/I011176/Downloads/IAV-CA-Bundle.crt'  # Set to the full path of your certificate
)


# Specify your bucket name
bucket_name = 'multi-modal-emotion-detection'
# Specify the local file path (adjust this to the correct path on your machine)
file_path = r'D:/Dataset/test.txt'  # Update this path to your actual file

normalized_file_path = os.path.abspath(file_path)  # Normalize the file path
print(f"Normalized file path: {normalized_file_path}")


file_name_in_s3 = 'Dataset'  # Adjusted to include the file name
# Check if the local file exists and has the right permissions
if not os.path.isfile(normalized_file_path):
    raise FileNotFoundError(f"The local file {normalized_file_path} does not exist.")
if not os.access(normalized_file_path, os.R_OK):
    raise PermissionError(f"The local file {normalized_file_path} is not readable.")


# Upload the file
try:
    response = s3_client.upload_file(file_path, bucket_name, 'destination-key')
    print(f"File uploaded successfully. {response}")
except Exception as e:
    print(f"Error uploading file: {e}")


