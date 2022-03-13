from django.contrib import admin
from .models import Film, Rating, Favorite


# Register your models here.
admin.site.register(Film)
admin.site.register(Rating)
admin.site.register(Favorite)


# INSERT INTO main_app_film(title, img, genre, plot, director, rated, released, metascore, imdbrating) VALUES('The Lord of the Rings: The Fellowship of the Ring', 'https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX300.jpg', 'Action, Adventure, Drama', 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.', 'Peter Jackson', 'PG-13', '19 Dec 2001', '92', '8.8');
# INSERT INTO main_app_film(title, img, genre, plot, director, rated, released, metascore, imdbrating) VALUES('The Lord of the Rings: The Two Towers', 'https://m.media-amazon.com/images/M/MV5BZGMxZTdjZmYtMmE2Ni00ZTdkLWI5NTgtNjlmMjBiNzU2MmI5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg', 'Action, Adventure, Drama', 'While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Saurons new ally, Saruman, and his hordes of Isengard.', 'Peter Jackson', 'PG', '18 Dec 2002', '87', '8.7');
# INSERT INTO main_app_film(title, img, genre, plot, director, rated, released, metascore, imdbrating) VALUES('The Lord of the Rings: The Return of the King', 'https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 'Action, Adventure, Drama', 'Gandalf and Aragorn lead the World of Men against Saurons army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.', 'Peter Jackson', 'PG-13', '17 Dec 2003', '94', '8.9');