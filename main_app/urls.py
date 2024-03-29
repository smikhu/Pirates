from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('favorites/', views.FavoritesList.as_view(), name="favorites"),
    path('navbar/', views.NavBar.as_view(), name="navbar"),
    path('new/', views.FilmCreate.as_view(), name="film_create"),
    path('film/<int:pk>/', views.FilmDetail.as_view(), name="film_detail"),
    path('film/<int:pk>/update', views.FilmUpdate.as_view(), name="film_update"),
    path('film/<int:pk>/delete', views.FilmDelete.as_view(), name="film_delete"),
    path('film/<int:pk>/ratings/new', views.RatingCreate.as_view(), name="rating_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('favorite/<int:film_pk>/add', views.AddFavorite.as_view(), name="add_favorite"),
    path('favorite/<int:favorite_pk>/remove', views.RemoveFavorite.as_view(), name="remove_favorite"),
]