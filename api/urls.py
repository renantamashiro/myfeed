from django.urls import path
from api import views

urlpatterns = [
    path("site-configs/", views.SiteConfigList.as_view(), name="site-config-list"),
    path("site-configs/<int:pk>/", views.SiteConfigDetail.as_view(), name="site-config-detail"),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail")
]