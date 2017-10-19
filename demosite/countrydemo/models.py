'''
Models for the Country Demo app
'''

from django.db import models
from django_countries.fields import CountryField


class CountryInfo(models.Model):
    '''
    A  model to demonstrate linking models with the `CountryField`
    '''
    country = CountryField()
    notes = models.TextField()

    def __repr__(self):
        return '{}'.format(self.country.name)

    def __str__(self):
        return str(self.__repr__())

    def __unicode__(self):
        return u'{}'.format(self.__repr__())


class LinkSet(models.Model):
    '''
    Defines a set of links to Country information on an external site
    A site can have different source types, so the 'host' field is not uniqwue
    But the 'label' and 'source_url' are unique.

    The source url is the URL of the aggregation/list page that links to specific countries.

    TODO: Change source_url to NOT be unique, so that we can make it null for sources that
    are not screen scraped
    '''
    label = models.CharField(max_length=100, unique=True)
    host = models.URLField()
    source_url = models.URLField(unique=True)

    def __repr__(self):
        return '{},{},{},{}'.format(self.id, self.label, self.host, self.source_url)

    def __str__(self):
        return str(self.__repr__())

    def __unicode__(self):
        return u'{}'.format(self.__repr__())


class CountryPageLink(models.Model):
    '''
    This model holds the country specific link to an external site.
    The set of these links per site are defined by the FK relationship
    to a LinkSet model instance
    '''

    country = CountryField()
    url = models.URLField(unique=True)
    linkset = models.ForeignKey(LinkSet, related_name='link_set')

    def __repr__(self):
        return '{},{},{}'.format(self.id, self.country, self.url,)

    def __str__(self):
        return str(self.__repr__())

    def __unicode__(self):
        return u'{}'.format(self.__repr__())
