from django.urls import path
from .views import EggsList, EggsDetail

urlpatterns = [
    path('', EggsList.as_view(), name='eggs_list'),
    path('<int:pk>', EggsDetail.as_view(), name='eggs-detail'),
]