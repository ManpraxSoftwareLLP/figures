from rest_framework.decorators import api_view
import boto3
import json
from django.core.cache import cache
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db import transaction
from django.views.decorators.http import require_POST
from figures.serializers import GeneralCourseDataSerializer
from .tasks import *
from rest_framework.response import Response

@api_view()
def get_course_csv_file(request):
    file_url = ''
    filename = cache.get('course_csv_file')
    file_status = cache.get('course_csv_status')
    try:
        if filename != '':
            s3 = boto3.client("s3",aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
            s3.head_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key='csv/{}'.format(filename))
            file_url = 'https://{}.s3.{}.amazonaws.com/csv/{}'.format(settings.AWS_STORAGE_BUCKET_NAME,settings.AWS_S3_REGION_NAME,filename)
    except:
        pass
    return Response({"file_url":file_url,'file_status':file_status, "status":200})

@api_view()
def get_userinfo_csv_file(request):
    file_url = ''
    filename = cache.get('user_csv_file')
    file_status = cache.get('user_csv_status')
    try:
        if filename != '':
            s3 = boto3.client("s3",aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
            s3.head_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key='csv/{}'.format(filename))
            file_url = 'https://{}.s3.{}.amazonaws.com/csv/{}'.format(settings.AWS_STORAGE_BUCKET_NAME,settings.AWS_S3_REGION_NAME,filename)
    except:
        pass
    return Response({"file_url":file_url, "status":200, "file_status":file_status})


