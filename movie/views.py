from django.shortcuts import render
from .models import Movie, Movie_links
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView

class MovieList(ListView):
    model = Movie
    paginate_by = 5



class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context


class MovieDetail(DetailView):
    model = Movie
    paginate_by = 5

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count +=1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail,self).get_context_data(**kwargs)
        context['links'] = Movie_links.objects.filter(movie=self.get_object())
        context['related_movies']= Movie.objects.filter(category=self.get_object().category)
        return context

class MovieCategory(ListView):
    model = Movie
    paginate_by = 5


    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category=self.category)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']= self.category
        return context

class MovieLanguage(ListView):
    model = Movie
    paginate_by = 5


    def get_queryset(self):
        self.language = self.kwargs['lang']
        movies = Movie.objects.filter(language=self.language)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_language']= self.language
        return context


class MovieSearch(ListView):
    model = Movie
    paginate_by = 5


    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()

        return object_list

#
# class MovieYear(YearArchiveView):
#     queryset = Movie.objects.all()
#     date_field = 'year_of_production'
#     make_object_list = True
#     allow_future = True
#
#     print(queryset)