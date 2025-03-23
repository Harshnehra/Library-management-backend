from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status,views
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import AdminUser
from .serializers import AdminSignupSerializer
import traceback


User = get_user_model()
class AdminSignupView(views.APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        
        if not username or not email or not password:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if AdminUser.objects.filter(email=email).exists():
            return Response({"error": "Email is already taken."}, status=status.HTTP_400_BAD_REQUEST)

        user = AdminUser.objects.create_user(username=username, email=email, password=password)

        return Response(
            {"id": user.id, "username": user.username, "email": user.email},
            status=status.HTTP_201_CREATED
        )

class AdminLoginView(views.APIView):
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        
        try:
            user = authenticate(email=email, password=password)
            
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                is_admin= User.objects.filter(email=email).values_list('isAdmin')
                
                return Response({"token": token.key,"is_admin": is_admin[0][0] }, status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            traceback.print_exec()
