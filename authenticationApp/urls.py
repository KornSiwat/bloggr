from django.urls import path
from authenticationApp.views import loginView

app_name = 'authenticationApp'

urlpatterns = [
    path('login/', loginView, name='login')
]
