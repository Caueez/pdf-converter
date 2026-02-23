import boto3

from infra.storage.interface import StorageInterface


class S3Storage(StorageInterface):
    def __init__(self, bucket: str)-> None:
        self._bucket = bucket
        self._s3_client = boto3.client("s3", region_name="us-east-1")

    def download_file(self, bucket_name, object_name, file_path):
        self._s3_client.download_file(bucket_name, object_name, file_path)

    def generate_presigned_url(self, object_name, expiration=3600):
        response = self._s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": self._bucket, "Key": object_name},
            ExpiresIn=expiration,
        )
        return response
