from django.urls import path

from .views import SearchView, ShowByIdView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('<int:show_id>/', ShowByIdView.as_view(), name='show_by_id'),
]