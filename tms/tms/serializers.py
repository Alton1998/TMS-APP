from rest_framework import serializers
from tmsapp.models import trafficAtD,trafficAtC,trafficAtB,trafficAtA
# serializing database data
class TrafficAtA(serializers.ModelSerializer):
    class Meta:
        model=trafficAtA
        fields = ('Trafficdensity','time')
class TrafficAtB(serializers.ModelSerializer):
    class Meta:
        model=trafficAtB
        fields = ('Trafficdensity','time')
class TrafficAtC(serializers.ModelSerializer):
    class Meta:
        model=trafficAtC
        fields = ('Trafficdensity','time')
class TrafficAtD(serializers.ModelSerializer):
    class Meta:
        model=trafficAtD
        fields = ('Trafficdensity','time')
