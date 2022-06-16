from .models import Hh_Request, Hh_Response
from .serializers import Hh_RequestSerializer, Hh_ResponseSerializer, BlogUserSerializer
from rest_framework import viewsets
from usersapp.models import BlogUser


class Hh_RequestViewSet(viewsets.ModelViewSet):
    queryset = Hh_Request.objects.all()
    serializer_class = Hh_RequestSerializer

class Hh_ResponseViewSet(viewsets.ModelViewSet):
    queryset = Hh_Response.objects.all()
    serializer_class = Hh_ResponseSerializer

class BlogUserViewSet(viewsets.ModelViewSet):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer