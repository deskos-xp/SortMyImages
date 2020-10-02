from django.shortcuts import render,redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http.response import HttpResponse,JsonResponse,Http404
from .models import ImagesTraining,ImagesUnuseable
from django.conf import settings
import json,os,base64,random
import tarfile
from io import BytesIO
#no auth this time around
# Create your views here.
def UploadImage_Training(request):
    context=dict()
    img=ImagesTraining()
    if 'file' in request.FILES.keys():
        img.img=request.FILES.get('file')
        img.save()
    return JsonResponse(context)

def UploadImage_Unuseable(request):
    context=dict()
    img=ImagesUnuseable()
    if 'file' in request.FILES.keys():
        img.img=request.FILES.get('file')
        img.save()
    return JsonResponse(context)

def EchoHello(request):
    return JsonResponse(dict(hello='hello'))

def export_useable(request):
    data=ImagesTraining.objects.filter().all()

    fileobj=BytesIO()
    with tarfile.open(fileobj=fileobj,mode='w|') as tar:
        for i in data:
            content=i.img.read()
            tf=tarfile.TarInfo(i.img.name)
            tf.size=len(content)
            tar.addfile(tf,BytesIO(content))
    fileobj.seek(0)
            
    #'''
    response=HttpResponse(fileobj.read(),content_type="data/octet-stream")
    response['Content-Disposition']='inline;filename='+'images.tar.xz'
    return response
    #'''
    #return HttpResponse('')
