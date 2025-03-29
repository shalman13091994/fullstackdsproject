from django.urls import path
from .views import prediction_data, customfileupload

from .views import Predictclassapi

urlpatterns = [
    path("predict", prediction_data, name="predict"),
    path('predictclass', Predictclassapi.as_view(), name = "predictclass"),

    #fileupload
    path('fileupload', customfileupload, name ='customfileupload')

]