from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r"home", views.AdvocateDetails.as_view(), basename="home")

urlpatterns = [
    # path("", views.AdvocateDetails.as_view(), name="home")
    path("advocates/", views.advocates_list, name="test"),
    path("advocates/<str:username>/", views.advocate_details, name="user"),
    path("companies/", views.company_details, name="company-list"),
    path("companies/<int:pk>/", views.company_details, name="company-detail"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
