
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Category, HelpType, Fund, Project, ProjectImage
from .serializers import (
    CategorySerializer,
    CategoriesMainListSerializer,
    HelpTypeSerializer,
    FundCreateSerializer,
    FundDetailSerializer,
    FundListSerializer,
    ProjectSerializer,
    ProjectCreateSerializer,
)
from .service import ProjectFilter

# Main

class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesMainListSerializer


class CatalogView(APIView):
    def get(self, request):
        response = {
            'categories': CategorySerializer(
                Category.objects.all(), many=True).data,
            'help_types': HelpTypeSerializer(
                HelpType.objects.all(), many=True).data
        }
        return Response(response)


# Funds

class FundListView(ListAPIView):
    queryset = Fund.objects.all()
    serializer_class = FundListSerializer


class FundViewSet(ViewSet):
    queryset = Fund.objects.all()

    def list(self, request):
        serializer = FundListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fund = get_object_or_404(self.queryset, pk=pk)
        serializer = FundDetailSerializer(fund)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = FundCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        serializer = FundCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


# Projects

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter


class ProjectViewSet(ViewSet):
    queryset = Project.objects.all()

    def retrieve(self, request, pk=None):
        project = get_object_or_404(self.queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProjectCreateSerializer(data=request.data)
        additional_images = []
        project_images = bool(request.data.get('additional_images'))
        if project_images:
            additional_images = request.data.pop('additional_images')
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            for img in additional_images:
                new_img = ProjectImage.objects.create(
                    image=img, project=project
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        serializer = ProjectCreateSerializer(data=request.data)
        additional_images = []
        project_images = bool(request.data.get('additional_images'))
        if project_images:
            additional_images = request.data.pop('additional_images')
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            for img in additional_images:
                new_img = ProjectImage.objects.create(
                    image=img, project=project
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
