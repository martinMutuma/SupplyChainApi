from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path

from auth.views import (
    SCTokenObtainPairView,
    UserRegisterView,
    UserListView,
    UserChangePasswordView
)

urlpatterns = [
    path(route='auth/login/', view=SCTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path(route='auth/register/',
         view=UserRegisterView.as_view(), name='user_register'),
    path(route='auth/token/refresh/',
         view=TokenRefreshView.as_view(), name='token_refresh'),
    path(route='auth/token/verify/',
         view=TokenVerifyView.as_view(), name='token_verify'),
    path(route='api/users/list/', view=UserListView.as_view(), name='user_list'),
    path(route='auth/password/',
         view=UserChangePasswordView.as_view(), name='user_password'),

]
