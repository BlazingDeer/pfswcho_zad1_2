from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import requests
import json

from . import forms

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class FibCalView(View):
    form_class = forms.Fib_seqForm
    template_name = "fib_cal.html"
    headers = {"Content-type": "application/json"}
    api_url = "http://api:8002/api/v1/fibseq/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        fib_seq_result = requests.get(self.api_url).json()
        wynik = None
        return render(
            request,
            self.template_name,
            {"form": form, "fib_seq_result": fib_seq_result, "wynik": wynik},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        wynik = None
        if form.is_valid():
            liczba = int(form.cleaned_data["number"])
            r_post = {
                "number": int(form.cleaned_data["number"]),
            }
            r = requests.post(self.api_url, json=r_post)
            print(r.status_code)
        else:
            form = self.form_class()

        resp = requests.get(self.api_url)
        fib_seq_result = resp.json()
        if fib_seq_result:
            wynik = fib_seq_result[0]

        return render(
            request,
            self.template_name,
            {"form": form, "fib_seq_result": fib_seq_result, "wynik": wynik},
        )


class FibDocsView(TemplateView):
    template_name = "fib_docs.html"
