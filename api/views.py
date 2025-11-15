from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets, filters
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .serializers import SignupSerializer, UserSerializer, MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

from .models import AdminMovie, Movie
from .serializers import AdminMovieSerializer, MovieSerializer
User = get_user_model()

# Auth
@api_view(['POST'])
def signup_view(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {"user": UserSerializer(user).data, "access": str(refresh.access_token), "refresh": str(refresh)}
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me_view(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

# Movies (list + create + detail)
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class MovieViewSet(viewsets.ModelViewSet):
    """
    - Staff: see all movies
    - Authenticated users: see only their movies
    - Anonymous: see none (empty list)
    """
    serializer_class = MovieSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre','platform','status','media_type']
    search_fields = ['title','director','genre','platform']
    ordering_fields = ['created_at','title','rating']
    ordering = ['-created_at']

    permission_classes = [IsOwnerOrReadOnly]  # keep your permission class

    def get_queryset(self):
        user = self.request.user
        qs = Movie.objects.all().order_by('-created_at')
        if user and user.is_authenticated:
            if user.is_staff:
                # staff/admin can see everything
                return qs
            # non-staff: only their own movies
            return qs.filter(user=user)
        # anonymous: return empty queryset
        return qs.none()

    def perform_create(self, serializer):
        user = self.request.user if self.request and self.request.user.is_authenticated else None
        serializer.save(user=user)



class AdminMovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdminMovie.objects.all().order_by('-created_at')
    serializer_class = AdminMovieSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'platform', 'media_type']
    search_fields = ['title', 'director', 'genre', 'platform']
    ordering_fields = ['created_at', 'title', 'rating']
    ordering = ['-created_at']

    permission_classes = [permissions.AllowAny]

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_from_admin_view(request, pk):
    """
    POST /api/movies/from-admin/<pk>/
    Copies AdminMovie(pk) into user's Movie and returns created Movie.
    """
    admin_item = get_object_or_404(AdminMovie, pk=pk)

    payload = {
        "title": admin_item.title,
        "media_type": admin_item.media_type,
        "director": admin_item.director,
        "genre": admin_item.genre,
        "platform": admin_item.platform,
        "total_episodes": admin_item.total_episodes,
        "episodes_watched": 0,
        "status": "wishlist",
        "rating": None,
        "review": ""
    }

    serializer = MovieSerializer(data=payload, context={'request': request})
    if serializer.is_valid():
        movie = serializer.save(user=request.user)
        return Response(MovieSerializer(movie, context={'request': request}).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
