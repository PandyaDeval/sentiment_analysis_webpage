from django import forms
class NameForm(forms.Form):
        tweet=forms.CharField(label='tweet',max_length=200)