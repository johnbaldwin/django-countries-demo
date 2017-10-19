'''

'''

import os
from textwrap import dedent

import yaml

from django.core.management.base import BaseCommand, CommandError

from django.conf import settings

from countrydemo.models import (
    LinkSet,
    CountryPageLink,
    )

def load_mapper_data(file):

    # Do transaction

    with open(file, 'r') as f:
        #try:
        data = yaml.load(f)
        #except yaml.YAMLError as e:

        #import pdb; pdb.set_trace()
        label = data['data_source']['label']
        host = data['data_source']['host']
        source_url = data['data_source']['url']
        linkset, created = LinkSet.objects.get_or_create(
            label=label,
            host=host,
            source_url=source_url,
            )
        country_links = data['country_links']
        if country_links:

            for row in country_links:
                print("Importing {}, {}".format(row['countrycode'], row['url']))
                cpl = CountryPageLink.objects.get_or_create(
                    url=row['url'],
                    country=row['countrycode'],
                    linkset=linkset,
                    )


class Command(BaseCommand):
    ''' 
    Seed our database
    '''
    help = dedent(__doc__).strip()

    def add_arguments(self, parser):
        '''

        '''
        parser.add_argument('--wikipedia',
            help='wikipedia link file to load',
            )

    def handle(self, *args, **options):
        if (options['wikipedia']):
            load_mapper_data(options['wikipedia'])
        else:
            print('No action. run ./manage.py import_data --help to see options')
