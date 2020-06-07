from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response 
from apps.account.api.serializer import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    """
    REGISTER NEW USER.
    """
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        