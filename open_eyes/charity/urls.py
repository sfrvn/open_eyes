from django.urls import path

from .views import (
    CatalogView,
    CategoriesListView,
    FundListView,
    FundViewSet,
    ProjectListView,
    ProjectViewSet,
)


urlpatterns = [
    path('', CategoriesListView.as_view()),
    path('catalog/', CatalogView.as_view()), # Список категорий, типов помощи (служебное) 

    path('funds/', FundViewSet.as_view({'get': 'list'})), # Список фондов
    path('funds/create/', FundViewSet.as_view({'post': 'create'})),
    path('funds/<int:pk>/', FundViewSet.as_view({'get': 'retrieve'})),
    path('funds/<int:pk>/update/', FundViewSet.as_view({'put': 'update'})),

    path('projects/', ProjectListView.as_view()),
    path('projects/create/', ProjectViewSet.as_view({'post': 'create'})),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve'})),
    path('projects/<int:pk>/update/', ProjectViewSet.as_view({'put': 'update'})),


    # TODO связь с фондом
    # TODO помощь администрации
]