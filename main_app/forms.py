from django import forms

from .models import Film


class FilmForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form"}))
    img = forms.CharField(widget=forms.TextInput)
    genre = forms.CharField(widget=forms.TextInput)
    plot = forms.CharField(widget=forms.Textarea)
    director = forms.CharField(widget=forms.TextInput)
    rated = forms.CharField(widget=forms.TextInput)
    released = forms.CharField(widget=forms.TextInput)
    metascore = forms.CharField(widget=forms.TextInput)
    imdbrating = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Film 
        fields = ['title', 'img', 'genre', 'plot', 'director', 'rated', 'released', 'metascore', 'imdbrating']