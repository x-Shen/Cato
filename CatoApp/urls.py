from django.conf.urls import url
from. import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$',views.login),
    url(r'^signup/$',views.sign_up)
]