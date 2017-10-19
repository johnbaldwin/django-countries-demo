
import logging

from django.core.urlresolvers import (
    reverse_lazy,
    )
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    DetailView,
    FormView,
    ListView,
    UpdateView,
    )
from django.views.generic.edit import FormMixin
from django_countries.widgets import CountrySelectWidget

from .forms import (
        UpdateCountryInfoForm,
        ChooseCountryForm,
    )
from .models import (
    CountryInfo,
    LinkSet,
    CountryPageLink,
)


logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'countrydemo/index.html', {})


def wikipedia_pages(request):
    '''
    Show the flags and links for wikipedia pages
    '''
    label = 'Wikipedia'
    linkset = LinkSet.objects.get(label=label)
    country_page_links = CountryPageLink.objects.filter(linkset=linkset)
    context = {
        'linkset': linkset,
        'country_page_links': country_page_links,
        'label': label,
    }
    return render(request, 'countrydemo/country_pages.html', context)


class CountryInfoListView(FormMixin, ListView):
    '''
    Provide countries
    '''

    model = CountryInfo
    template_name = 'countrydemo/country_info_list.html'
    form_class = ChooseCountryForm
    def get_context_data(self, **kwargs):
        context = super(CountryInfoListView, self).get_context_data(**kwargs)
        
        return context

    def get_success_url(self):
        logger.info('CountryInfoListView.get_success_url called...')
        return reverse('country-info-list-view')

    def post(self, request, *args, **kwargs):
        logger.info('CountryInfoListView.post called')
        logger.info('args={}'.format(args))
        logger.info('kwargs={}'.format(kwargs))

        country = request.POST.get('country')
        country_info = CountryInfo.objects.get(country=country)
        context = { 'pk': country_info.pk}

        return HttpResponseRedirect(reverse('countrydemo:country-info-detail-view',
            kwargs={ 'pk': country_info.pk}))


class CountryInfoDetailView(DetailView):
    '''

    '''

    model = CountryInfo
    template_name = 'countrydemo/country_info_detail.html'

    def get_info_links(self):
        return CountryPageLink.objects.filter(country=self.object.country)

    def get_context_data(self, **kwargs):
        context = super(CountryInfoDetailView, self).get_context_data(**kwargs)
        context['info_links'] = self.get_info_links()
        return context


class CountryInfoUpdateView(UpdateView):
    '''

    '''

    context_object_name = 'country_info'
    form_class = UpdateCountryInfoForm
    template_name = 'countrydemo/country_info_update_form.html'

    def get_object(self, queryset=None):
        return CountryInfo.objects.get(id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('countrydemo:country-info-detail-view',
            kwargs={ 'pk': self.object.pk })
