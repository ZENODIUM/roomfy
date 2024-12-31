from django import forms
from .models import Profile
from django.forms import formset_factory

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'photo', 'birthday','post1','post2','post3', 'favorite_music', 'social_links', 
            'favorite_books', 'favorite_movies', 'favorite_food', 'room_background','country','link1','link2','link3','link4'
        ]
        widgets = {
            'room_background': forms.TextInput(attrs={'type': 'color'}),
        }

class SocialLinkForm(forms.Form):
    link = forms.URLField(required=False, label="Social Link")

# Create a formset for multiple social links
SocialLinkFormSet = formset_factory(SocialLinkForm, extra=5)  # Allow up to 6 links (1 + 5 extra)
