from .models import Hh_Request, Hh_Response
from .serializers import Hh_RequestSerializer, Hh_ResponseSerializer, BlogUserSerializer
from rest_framework import viewsets
from usersapp.models import BlogUser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
# from .permissions import ReadOnly, IsAuthor


class Hh_RequestViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Hh_Request.objects.all()
    serializer_class = Hh_RequestSerializer

class Hh_ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Hh_Response.objects.all()
    serializer_class = Hh_ResponseSerializer

class BlogUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer