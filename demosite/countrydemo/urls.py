from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', TemplateView.as_view(
        template_name='countrydemo/about.html'),
        name='country-demo-about'),
    url(r'^country-pages/', views.wikipedia_pages,
        name='country-pages'),
    url(r'^info/$', views.CountryInfoListView.as_view(),
        name='country-info-list-view'),
    url(r'^info/(?P<pk>\d+)/$', views.CountryInfoDetailView.as_view(),
        name='country-info-detail-view'),
    url(r'^info/update/(?P<pk>\d+)', views.CountryInfoUpdateView.as_view(),
        name='country-info-update-view'),
]
