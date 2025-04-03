from django.http import HttpResponse
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from rest_framework.views import APIView
from rest_framework import status
import os
import shutil

from src.DiamondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline, CustomDataUpload

@api_view(['GET', 'POST'])
def prediction_data(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET' or "POST":

        data = CustomData(
        carat = request.POST.get('carat'),
        depth = request.POST.get('depth'),
        table = request.POST.get('table'),
        x = request.POST.get('x'),
        y = request.POST.get('y'),
        z = request.POST.get('z'),
        cut = request.POST.get('cut'),
        color = request.POST.get('color'),
        clarity = request.POST.get('clarity')

        )
        
        df = CustomData.get_as_dataframe(data)

        Prediction_data = PredictPipeline()
        result = Prediction_data.predict_data(df)


        return Response(f"The price is {result[0]:.2f}")



#creating class based views
class Predictclassapi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        try: 

            data = CustomData(
            carat = request.POST.get('carat'),
            depth = request.POST.get('depth'),
            table = request.POST.get('table'),
            x = request.POST.get('x'),
            y = request.POST.get('y'),
            z = request.POST.get('z'),
            cut = request.POST.get('cut'),
            color = request.POST.get('color'),
            clarity = request.POST.get('clarity')

            )
            
            df = CustomData.get_as_dataframe(data)

            Prediction_data = PredictPipeline()
            result = Prediction_data.predict_data(df)


            return Response(f"The price is {result[0]:.2f}", status=status.HTTP_200_OK)

        except Exception as e:    
           return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        
        try:

            data = CustomData(
            carat = request.POST.get('carat'),
            depth = request.POST.get('depth'),
            table = request.POST.get('table'),
            x = request.POST.get('x'),
            y = request.POST.get('y'),
            z = request.POST.get('z'),
            cut = request.POST.get('cut'),
            color = request.POST.get('color'),
            clarity = request.POST.get('clarity')

            )
            
            df = CustomData.get_as_dataframe(data)

            Prediction_data = PredictPipeline()
            result = Prediction_data.predict_data(df)


            return Response(f"The price is {result[0]:.2f}",  status=status.HTTP_200_OK)

        except Exception as e:    
           return Response(e, status=status.HTTP_400_BAD_REQUEST)

#save and upload file
def filemovement(uploaded_file):
    
    path = r"D:\Datascience\fullstackdsproject\Api\api"
    upload_dir = os.path.join(path, 'Fileupload')
    os.makedirs(upload_dir, exist_ok=True)  # Create directory if it doesn't exist

    file_name = os.path.basename(path) 

    file_path = os.path.join(upload_dir, file_name)
    with open(file_path, 'wb') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)
    
    return file_path


#uploading the file

@api_view(['GET', 'POST'])
def customfileupload(request):

        if 'file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_file = request.FILES['file']  # Get the uploaded file


        # # Define file path to save
        upload_dir = os.path.join(r"D:\Datascience\fullstackdsproject\Api\api\Fileupload")
        os.makedirs(upload_dir, exist_ok=True)  # Create directory if not exists


        file_path = os.path.join(upload_dir, uploaded_file.name)
        print(file_path)
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)


        # Convert uploaded file to DataFrame
        custom_upload_data = CustomDataUpload()  # Instance
        df = custom_upload_data.get_as_dataframe(file_path)


        Prediction_data = PredictPipeline()
        result = Prediction_data.predict_data(df)

        #merging with the predicted price with raw data
        finaldf_merged = pd.concat([df, result], axis=1)

        # export to output file
     
        output_dir =  os.path.join(r"D:\Datascience\fullstackdsproject\Api\api\output")# Create directory if not exists
        os.makedirs(output_dir, exist_ok=True)

        finaldf_merged.to_csv(r"D:\Datascience\fullstackdsproject\Api\api\output\mergedoutput.csv")    
        
        # this will read n write the file into dataframes
        file_path = os.path.join(output_dir,"output")
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        
        return Response(f"The price is {finaldf_merged.head(5)}",  status=status.HTTP_200_OK) 
        # return Response(f"The price is {result[0]:.2f}",  status=status.HTTP_200_OK)


