from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import SignupSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@api_view(['POST'])
def signup_view(request):
    """
    POST /api/auth/signup/
    Accepts: { email, password, confirm_password, first_name?, last_name? }
    Returns JWT access & refresh tokens on success + user data
    """
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # create token pair
        refresh = RefreshToken.for_user(user)
        data = {
            "user": UserSerializer(user).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Use SimpleJWT's TokenObtainPairView for /api/auth/login/
class LoginView(TokenObtainPairView):
    # default serializer returns access & refresh tokens if credentials ok
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me_view(request):
    """
    GET /api/auth/me/  (protected)
    Returns current user info
    """
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)