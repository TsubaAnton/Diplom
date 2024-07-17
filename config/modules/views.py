from rest_framework import generics
from .models import Modules
from .serializers import ModulesSerializer
from .paginators import ModulesPaginator
from rest_framework.permissions import IsAuthenticated


class ModulesListAPIView(generics.ListAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    pagination_class = ModulesPaginator
    permission_classes = [IsAuthenticated]


class ModulesCreateAPIView(generics.CreateAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    permission_classes = [IsAuthenticated]


class ModulesRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    permission_classes = [IsAuthenticated]


class ModulesUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    permission_classes = [IsAuthenticated]


class ModulesDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ModulesSerializer
    queryset = Modules.objects.all()
    permission_classes = [IsAuthenticated]

