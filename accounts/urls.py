from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    #
    path("login" , views.login_views , name = "login"),
    #logout
    # path("logout" , views.logout_views , name = "logout"),
    #registration / signup
    path("signup" , views.signup_views , name = "signup")
]