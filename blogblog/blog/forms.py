__author__ = 'wikibootup'

from django import forms

#class PostsForm(forms.Form):
#    subjects = forms.CharField(max_length=100)
#                               , widget=forms.TextInput(attrs="class":'form-control'))
#    content = forms.CharField(widget=forms.Textarea)
#    writer = forms.CharField(max_length=50)

from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts