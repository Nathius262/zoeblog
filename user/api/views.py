from ..models import Account
from .serializer import *
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


# page size
class SetUsersPaginationResult(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


#get the details of the anthenticated user to edit...
class UserProfileSetting(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserProfileDetailedSerializer
    queryset = Account.objects.all()
    lookup_field = 'username'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        if str(username) == str(request.user):
            return self.retrieve(request)
        else:
            user = username
            return Response({'response': f"You're not authenticated as {user}"})

    def put(self, request, username):
        return self.update(request)
        
    def destroy(self, request, username):
        return self.destroy(request)

#get the list of all users
class UserProfileGenericView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    serializer_class = UserProfileSerializer
    queryset = Account.objects.all()
    lookup_field = 'username'
    pagination_class = SetUsersPaginationResult

    def get(self, request, username=None):

        if username:
            return self.retrieve(request)
        else:
            return self.list(request)
    
@api_view(['post',])
def signup_view(request):
    serializer = UserProfileSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data = {
            'response': "successfully registered a new user",
            'email': account.email,
            'username': account.username,
            'token': Token.objects.get(user=account).key,
        }
    else:
        data = serializer.errors
    return Response(data)