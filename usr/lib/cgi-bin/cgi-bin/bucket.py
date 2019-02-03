# Kyle Stead kstead2016@my.fit.edu
from sys import argv
from google.cloud import storage
import datetime

class Bucket_Manager:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket = storage_client.get_bucket("mediosk-data")
    
    def upload(self, file_name, data, silent=True):
        if data:
            # Create a timestamp for the file name, and slap a .json on there
            file_name = int((datetime.datetime.today()- datetime.datetime(1970,1,1)).total_seconds()) + ".json"
            # Select the blob we are writing to, and upload the string
            blob = self.bucket.blob(file_name)
            blob.upload_from_string(data)
            if not silent:
                print('Uploaded to {}.'.format(
                    file_name))
    def list(self):
        blobs = self.bucket.list_blobs()

        for blob in blobs:
            print(blob.name)
        
# Google provided samples below #
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print('Blob {} deleted.'.format(blob_name))
