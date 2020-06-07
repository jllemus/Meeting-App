from django.shortcuts import render, redirect
# REST FRAMEWORK
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.website.forms import MeetingForm
from apps.website.models import Meeting
from apps.website.api.serializer import MeetingSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

class MeetingApi(APIView):
    """
    Returns all meeting objects in the database
    """
    def get(self, request):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetToken(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.get_or_create(user=request.user)
        print(Token)
        return render(request, 'apps/website/token.html', {'token': token})