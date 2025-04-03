from django.urls import path

from .views import prediction_data, customfileupload, Predictclassapi

urlpatterns = [
    path("predict", prediction_data, name="predict"),
    
    #class method
    path('predictclass', Predictclassapi.as_view(), name = "predictclass"),

    #fileupload
    path('fileupload', customfileupload, name ='customfileupload')

]