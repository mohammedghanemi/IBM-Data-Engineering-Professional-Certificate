'''
import boto3
import os

# Set environment variables for the credentials (optional but recommended)
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
folder_path = r'D:/CREMA-D/CREMA-D_FSLF/train'  # Update this path to your actual file
# Define the name of the folder you want to create in S3
s3_folder_name = 'cremadfirstload'  # The name of the folder in the S3 bucket

normalized_file_path = os.path.abspath(folder_path)  # Normalize the file path
print(f"Normalized file path: {normalized_file_path}")

# Marcher 3la tous les fichiers fi dossier w sbathom l'S3
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)  # Chemin complet
        s3_key = os.path.join(s3_folder_name, os.path.relpath(file_path, folder_path)).replace("\\", "/")  # Clef S3 (format UNIX)
        
        try:
            # Upload fichier vers S3
            s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"File {file_path} uploaded to {bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}")
'''

import boto3
import os

# Set environment variables for the credentials (optional but recommended)
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
folder_path = r'D:/CREMA-D/CREMA-D_FSLF/train'  # Update this path to your actual file
# Define the name of the folder you want to create in S3
s3_folder_name = 'cremadfirstload'  # The name of the folder in the S3 bucket

normalized_file_path = os.path.abspath(folder_path)  # Normalize the file path
print(f"Normalized file path: {normalized_file_path}")

# Limit the number of files to upload
max_files = 1000
file_count = 0

# Walk through all the files in the folder and upload them to S3
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file_count >= max_files:
            print(f"Limit of {max_files} files reached.")
            break
        file_path = os.path.join(root, file)  # Full file path
        s3_key = os.path.join(s3_folder_name, os.path.relpath(file_path, folder_path)).replace("\\", "/")  # S3 key (Unix format)
        
        try:
            # Upload the file to S3
            s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"File {file_path} uploaded to {bucket_name}/{s3_key}")
            file_count += 1
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}")
    
    if file_count >= max_files:
        break

print(f"Total files uploaded: {file_count}")
