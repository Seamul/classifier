from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestModel


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})

    def post(self, request):
        # {
        #     "message": "Hello, World!"
        # }
        request_data = request.data.copy()
        TestModel.objects.create(test_field=request_data['message'])
        return Response(request_data)


# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .utils import predict_label  # Assuming predict_label function is defined in utils.py

class TitleClassificationView(APIView):

    def post(self, request, *args, **kwargs):
        # Log an info message (optional)
        print("Classifier Requested")

        data = request.data
        layout_xml_paths = data.get('layout_xml_paths', None)
        category = data.get('category', None)
        memory_points = data.get('memory_points', None)
        get_real_label = data.get('get_real_label', False)

        if not layout_xml_paths:
            error = "layout_xml_paths not found."
            print(error)
            return JsonResponse({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        # Assuming predict_label function is defined in utils.py
        doctypes = predict_label(layout_xml_paths, category, memory_points, get_real_label)

        response_data = {"doctypes": doctypes}
        print(f"Response: {response_data}")

        return JsonResponse(response_data, status=status.HTTP_200_OK)

