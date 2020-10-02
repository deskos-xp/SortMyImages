from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #path('upload_testing/',csrf_exempt(views.UploadImage_Testing),name='upload_testing'),
    path('upload_training/',csrf_exempt(views.UploadImage_Training),name='upload_training'),
    path('upload_unuseable/',csrf_exempt(views.UploadImage_Unuseable),name='upload_unuseable'),
    path('hello/',views.EchoHello,name='echo'),
    path('export/',views.export_useable,name='export'),
]
