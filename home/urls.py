from django.urls import path
from .views import admin_sahifa, Home_Page_Veiw
app_name='home'

urlpatterns = [
    path("", Home_Page_Veiw.as_view(), name="home"),

    path('admins', admin_sahifa, name='admins'),
]