from rest_framework import routers, serializers, viewsets
from .models import Hh_Request, Hh_Response
from usersapp.models import BlogUser

class Hh_RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hh_Request
        fields = '__all__'
        # fields = ['id', 'keywords', 'create', 'update']

class Hh_ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hh_Response
        fields = '__all__'

class BlogUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogUser
        # fields = '__all__'
        fields = ['username','email', 'is_dbAdmin']