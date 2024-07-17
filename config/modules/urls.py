from django.urls import path
from .views import (ModulesListAPIView, ModulesCreateAPIView, ModulesRetrieveAPIView,
                    ModulesUpdateAPIView, ModulesDestroyAPIView)
from .apps import ModulesConfig

app_name = ModulesConfig.name

urlpatterns = [
    path('modules/', ModulesListAPIView.as_view(), name='modules_list'),
    path('modules/create/', ModulesCreateAPIView.as_view(), name='modules_create'),
    path('modules/<int:pk>/', ModulesRetrieveAPIView.as_view(), name='modules_retrieve'),
    path('modules/update/<int:pk>', ModulesUpdateAPIView.as_view(), name='modules_update'),
    path('modules/delete/<int:pk>', ModulesDestroyAPIView.as_view(), name='modules_destroy'),
]
