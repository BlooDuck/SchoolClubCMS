from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    #author = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Author...'}))
    #body = forms.CharField(label='', max_length=400, widget=forms.Textarea(attrs={'class':'form-control form-control-sm', 'placeholder':'Comment...', 'rows':'3'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Author...'})
        self.fields['body'].widget.attrs.update({'class':'form-control form-control-sm editable', 'placeholder':'Comment...', 'rows':'3'})

        # Remove labels from generated forms
        self.fields['author'].label = ''
        self.fields['body'].label = ''

    class Meta:
        model = Comment
        fields = ('author', 'body')


