from django.conf.urls import url
from django.urls import path
import nlp.views

app_name = 'nlp'

urlpatterns = [
  path('', nlp.views.ResultView.as_view()),
  ]
  