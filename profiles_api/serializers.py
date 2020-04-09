from rest_framework import serializers

"""
A serializer is a feature of django rest framework

data input  --->  python object  (and vice versa)

similar to a django form. - define fields for your input to your api.

"""
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    