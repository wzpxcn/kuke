from django.conf.urls import url
from choice import views

app_name = 'choice'
urlpatterns = [
    url(r'^$',views.index,name='index'),
]