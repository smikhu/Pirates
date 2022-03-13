from time import time
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Film, Rating, Favorite
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# class Movie:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

# movies = [
#     Movie("The Lord of the Rings: The Fellowship of the Ring", "https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX300.jpg", "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron."),
#     Movie("The Lord of the Rings: The Two Towers", "https://m.media-amazon.com/images/M/MV5BZGMxZTdjZmYtMmE2Ni00ZTdkLWI5NTgtNjlmMjBiNzU2MmI5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg", "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard."),
#     Movie("The Lord of the Rings: The Return of the King", "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg", "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.")
# ]


# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["movies"] = movies
    #     return context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["films"] = Film.objects.all()
        title = self.request.GET.get("title")
        if title != None:
            context["films"] = Film.objects.filter(title__icontains=title)
        else:
            context["films"] = Film.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class FavoritesList(TemplateView):
    template_name = "favorites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.filter(user=self.request.user)



        return context

class AddFavorite(View):
    def get(self, request, film_pk):
        current_film = Film.objects.get(pk=film_pk)
        favorite = Favorite.objects.create(user=self.request.user, title=current_film.title, img=current_film.img, film=current_film)
        return redirect('favorites')

class RemoveFavorite(View):
    def get(self, request, favorite_pk):
        favorite = Favorite.objects.get(pk=favorite_pk)
        favorite.delete()
        return redirect('favorites')


class NavBar(TemplateView):
    template_name = "navbar.html"

class FilmCreate(CreateView):
    model = Film
    fields = ['title', 'img', 'genre', 'plot', 'director', 'rated', 'released', 'metascore', 'imdbrating']
    template_name = "film_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FilmCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('film_detail', kwargs={'pk': self.object.pk})

class FilmDetail(DetailView):
    model = Film 
    template_name = "film_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # interactions of query sets
        all_films = Film.objects.all()
        all_favorites = Favorite.objects.filter(user=self.request.user).values_list('title', flat=True)
        # 
        print(all_favorites)
        available = all_films.exclude(title__in=all_favorites)
        print(available)
        context['available'] = available
        return context

class FilmUpdate(UpdateView):
    model = Film
    fields = ['title', 'img', 'genre', 'plot', 'director', 'rated', 'released', 'metascore', 'imdbrating']
    template_name = "film_update.html"
    def get_success_url(self):
        return reverse('film_detail', kwargs={'pk': self.object.pk})

class FilmDelete(DeleteView):
    model = Film
    template_name = "film_delete_confirmation.html"
    success_url = '/'

class RatingCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        score = request.POST.get("score")
        comment = request.POST.get("comment")
        film = Film.objects.get(pk=pk)
        Rating.objects.create(name=name, score=score, comment=comment, film=film)
        return redirect('film_detail', pk=pk)
    
    def main_view(request):
        obj = Rating.objects.filter(score=0).order_by("?").first()
        context = {
            "object": obj
        }
        return render(request, 'main_app/film_detail.html', context)

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


# query sets
