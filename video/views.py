import os
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
@api_view(['POST'])
def upload_file(request):

    # print(request.FILES)
    file_obj = request.FILES['file']


    # organize a path for the file in bucket
    if file_obj.name.split('.')[-1].lower() == 'mp4':
        file_directory_within_bucket = 'video'  
    else:
        file_directory_within_bucket = 'image'


    # generate the file path
    file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            file_obj.name
        )


    if not default_storage.exists(file_path_within_bucket):
        default_storage.save(file_path_within_bucket, file_obj)
        file_url = default_storage.url(file_path_within_bucket)

        return JsonResponse({
                'message': 'OK',
                'fileUrl': file_url,
            },status=200)
    
    else:    
        return JsonResponse({
            'Message': 'Error: Filename already exists'
            
        })
