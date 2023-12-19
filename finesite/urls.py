
from django.urls import path, include

urlpatterns = [
    path('', include('authentification.urls')),
    path('', include('app.urls'))
]
