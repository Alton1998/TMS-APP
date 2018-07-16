from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrafficAtA,TrafficAtB,TrafficAtC,TrafficAtD
from tmsapp.models import trafficAtA,trafficAtB,trafficAtC,trafficAtD
# defining functionalities of apis using class based views and also defining the permissions to access data through functions defined in the classes
class ListTrafficAtA(APIView):
    def get(self,request):
        data=trafficAtA.objects.all()
        serializer=TrafficAtA(data,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TrafficAtA(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ListLatestTrafficAtA(APIView):
    def get(self,request):
        data = trafficAtA.objects.all().order_by('id')
        lastEnteredData=data.reverse()[:1]
        serializer=TrafficAtA(lastEnteredData,many=True)
        return Response(serializer.data)
class ListTrafficAtB(APIView):
    def get(self,request):
        data=trafficAtB.objects.all()
        serializer=TrafficAtB(data,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TrafficAtB(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ListTrafficAtC(APIView):
    def get(self,request):
        data=trafficAtC.objects.all()
        serializer=TrafficAtC(data,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TrafficAtC(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ListTrafficAtD(APIView):
    def get(self,request):
        data=trafficAtD.objects.all()
        serializer=TrafficAtD(data,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TrafficAtD(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
