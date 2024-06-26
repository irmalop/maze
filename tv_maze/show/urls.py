from django.urls import path

from .views import SearchView, ShowByIdView, CommentView, RatingView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('<int:show_id>/', ShowByIdView.as_view(), name='show_by_id'),
    path('comment/', CommentView.as_view(), name='shows_comment'),
    path('<int:show_id>/rating/', RatingView.as_view(), name='rating'),
]