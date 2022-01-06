from django import forms


class Fib_seqForm(forms.Form):
    number = forms.IntegerField(min_value=0, max_value=20, label="Wprowadź k:")
