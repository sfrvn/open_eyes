from django_filters import rest_framework as filters

from .models import Project


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProjectFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Project
        fields = ['category',]
