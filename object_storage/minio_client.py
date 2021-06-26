
from minio import Minio

from dotenv import load_dotenv
import os

load_dotenv()

MINIO_ACCESS_KEY = os.getenv('MINIO_ROOT_USER')
MINIO_SECRET_KEY = os.getenv('MINIO_ROOT_PASSWORD')
MINIO_URL = os.getenv('MINIO_URL')

client = Minio('localhost:9001',secure=False, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY )