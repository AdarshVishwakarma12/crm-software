from rest_framework import generics, permissions

from django.contrib.auth.models import User

from accounts.models import (
    BusinessUser,
    Role,
    AccessPermission,
)

from client.models import (
    Project,
    ProjectAccessPermission,
    Client,
    Document,
    Task,
    ActivityLog,
)

from .serializers import (
    UserSerializer,
    BusinessUserSerializer,
    ProjectSerializer,
    ClientSerializer,
    DocumentSerializer,
    TaskSerializer,
    ActivityLogSerializer,
)

class AndroidSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class AndroidDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "total_leads": Client.objects.count(),
            "total_tasks": Task.objects.count(),
            "total_roles": Role.objects.count(),
        })

class AndroidProjectView(generics.ListAPIView):
    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            userFromRequest = self.request.user
            businessUserFromRequest = BusinessUser.objects.get(user = userFromRequest)
            projectQuerySetFromRequest = Project.objects.filter(user = businessUserFromRequest)
            return projectQuerySetFromRequest
        except:
            pass

        return Project.objects.none()

class AndroidClientListView(generics.ListAPIView):
    # queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            userFromRequest = self.request.user
            businessUserFromRequest = BusinessUser.objects.get(user = self.request.user)
            ClientQuerySetFromRequest = Client.objects.filter(companyAssignee = businessUserFromRequest)
            return ClientQuerySetFromRequest
        except:
            pass
        return Client.objects.none()

class AndroidDocumentView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AndroidTaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class AndroidActivityLogView(generics.ListAPIView):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

# class RoleListView(generics.ListAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer


# Social Account
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from dj_rest_auth.serializers import JWTSerializer
from dj_rest_auth.registration.serializers import SocialLoginSerializer

# Google Authentication
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class GoogleLoginJWT(SocialLoginView):
    # authentication_classes = [JWTCookieAuthentication]
    # serializer_class = SocialLoginSerializer
    adapter_class = GoogleOAuth2Adapter
    # response_serializer = JWTSerializer

# Microsoft Authentication
from allauth.socialaccount.providers.microsoft.views import MicrosoftGraphOAuth2Adapter

class MicrosoftLoginJWT(SocialLoginView):
    adapter_class = MicrosoftGraphOAuth2Adapter