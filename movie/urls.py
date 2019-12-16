from django.urls import path
from .views import MovieDetail,MovieList,MovieCategory,MovieLanguage,MovieSearch
# gore ako ikad to napravim MovieYear
app_name = 'movie'

urlpatterns = [
    path('',MovieList.as_view(), name='movie_list'),
    path('category/<str:category>',MovieCategory.as_view(), name='movie_category'),
    path('langugage/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    # path('year/<int:year>', MovieYear.as_view(), name='movie_year'),

]