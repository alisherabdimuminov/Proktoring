from django.urls import path

from .views import create_blocked_application, get_blocked_applications_list


urlpatterns = [
    path('create/', create_blocked_application, name="create"),
    path('get/', get_blocked_applications_list, name='get'),
]