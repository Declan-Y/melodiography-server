
from minio import Minio

from dotenv import load_dotenv
import os

load_dotenv()

MINIO_ACCESS_KEY = os.getenv('MINIO_ROOT_USER')
MINIO_SECRET_KEY = os.getenv('MINIO_ROOT_PASSWORD')
MINIO_URL = os.getenv('MINIO_URL')
SECURE = os.getenv('SECURE')

# client = Minio(MINIO_URL,secure=False, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY )
client = Minio('minio1:9000',secure=False, access_key='admin', secret_key='password' )