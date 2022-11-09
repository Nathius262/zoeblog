from ..models import BlogPost
from .serializer import BlogPostSerializer
from rest_framework import mixins, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from user.models import Account

# page size
class SetBlogPostPaginationResult(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BlogPostViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'slug'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = SetBlogPostPaginationResult
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body', 'author__username', 'category__category_name', ]

    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request)
        else:
            return self.list(request)            

    def put(self, request, slug=None):
        obj = BlogPost.objects.all().filter(slug=slug).first()
        if str(request.user) == str(obj.author):
            return self.update(request)
        else:
            return Response({'response': f'You do not have access to write this post; You are not an author of "{obj.title}"'})

    def delete(self, request, slug=None):
        obj = BlogPost.objects.all().filter(slug=slug).first()
        if str(request.user) == str(obj.author):
            self.destroy(request)
            return Response({'response': f'"{obj.title}" has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'response': f'You do not have access to delete this post; You are not an author of "{obj.title}"'})


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def create_post_view(request):
    # get the author of the blog post
    account = request.user
    blog_post = BlogPost(author=account)
    serializer = BlogPostSerializer(blog_post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)