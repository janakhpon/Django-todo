from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=120,
    widget=forms.Textarea(
        attrs={
            'class':'form-input',
            'placeholder':'Hello there! 👋👋 .. ',
            'rows':'10'
        }
    ))

