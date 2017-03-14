from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search),
    url(r'^data/json/skills/all/$',views.json_all_skills),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),
    url(r'^signup/$',views.sign_up),
    url(r'^profile/$',views.profile),
]