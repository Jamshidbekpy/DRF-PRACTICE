from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# for login and refresh
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# for register and logout

from .views import RegisterView, LogoutView

urlpatterns += [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]


# show profile and change password
from .views import ShowProfile 

urlpatterns += [
    path('api/profile/', ShowProfile.as_view(), name='show_profile'),
    # path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
]

# channel retrieve,create,update and delete
from .views import ChannelCreateAPIView

urlpatterns += [
    path('api/channel/', ChannelCreateAPIView.as_view(), name='channel_create'),
    # path('api/channel/<int:pk>/', ChannelRetrieveAPIView.as_view(), name='channel_retrieve'),
    # path('api/channel/<int:pk>/update/', ChannelUpdateAPIView.as_view(), name='channel_update'),
    # path('api/channel/<int:pk>/delete/', ChannelDeleteAPIView.as_view(), name='channel_delete'),
]