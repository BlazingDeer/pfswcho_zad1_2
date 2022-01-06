from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("fibcalc", views.FibCalView.as_view(), name="fib_cal"),
    path("fibdocs", views.FibDocsView.as_view(), name="fib_docs"),
]
