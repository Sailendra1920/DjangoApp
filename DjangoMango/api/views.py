from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Username
from .serializer import UsernameSerializer


@api_view(['GET'])
def getData(request):
    names = Username.objects.all()
    serializer = UsernameSerializer(names, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = UsernameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)