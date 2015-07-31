from django.conf.urls import include, url   # importando métodos do django
from . import views                         # importando todas as views do blog


urlpatterns = [
    url(r'^$', views.post_list),
]
