import time

from rest_framework import serializers

from .models import Category, HelpType, Fund, Project, ProjectImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class HelpTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpType
        fields = ('id', 'title',)


# Funds

class FundListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    projects_count = serializers.SerializerMethodField()

    def get_projects_count(self, fund):
        return Project.objects.filter(fund=fund).count()


    class Meta:
        model = Fund
        fields = ('id', 
            'name',
            'city',
            'projects_count',
            'logo',
            'phone',
            'url',
            'categories',
        )


class FundCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = (
            'id', 
            'name',
            'description',
            'city',
            'logo',
            'phone',
            'url',
            'categories',
        )


class FundDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Fund
        fields = (
            'id', 
            'name',
            'description',
            'city',
            'logo',
            'phone',
            'url',
            'categories',
        )


class FundShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ('id', 
            'name',
            'city',
            'phone',
            'url',
            'logo',
        )


# Project

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'image',)


class ProjectSerializer(serializers.ModelSerializer):
    fund = FundShortSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    help_type = HelpTypeSerializer(read_only=True)
    published_at = serializers.SerializerMethodField()
    additional_images = ProjectImageSerializer(read_only=True, many=True)

    def get_published_at(self, project):
        return time.mktime(project.published_at.timetuple())

    class Meta:
        model = Project
        fields = (
            'id', 
            'name',
            'description',
            'short_description',
            'fund',
            'category',
            'help_type',
            'help_description',
            'city',
            'published_at',
            'main_image',
            'additional_images',
        )


class ProjectShortSerializer(serializers.ModelSerializer):
    fund = FundShortSerializer(read_only=True)
    help_type = HelpTypeSerializer(read_only=True)
    published_at = serializers.SerializerMethodField()

    def get_published_at(self, project):
        return time.mktime(project.published_at.timetuple())

    class Meta:
        model = Project
        fields = ('id', 
            'name',
            'short_description',
            'fund',
            'help_type',
            'help_description',
            'city',
            'published_at',
            'main_image',
        )


class ProjectCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Project
        fields = (
            'id', 
            'name',
            'description',
            'short_description',
            'fund',
            'category',
            'help_type',
            'help_description',
            'city',
            'published_at',
            'main_image',
            'additional_images',
        )


class CategoriesMainListSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()

    def get_projects(self, category):
        qs = Project.objects.filter(category=category).order_by('-published_at')
        return ProjectShortSerializer(qs[3], many=True).data

    class Meta:
        model = Category
        fields = ('id', 'title', 'projects')


class CatalogSerializer(serializers.Serializer):
    categories = serializers.SerializerMethodField()
    help_types = serializers.SerializerMethodField()

    def get_categories(self):
        qs = Category.objects.all()
        return CategorySerializer(qs, many=True).data
    
    def get_help_types(self):
        qs = HelpType.objects.all()
        return HelpTypeSerializer(qs, many=True).data
    
    class Meta:
        fields = ('id', 'categories', 'help_types')