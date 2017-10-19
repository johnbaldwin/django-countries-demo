
from textwrap import dedent

import yaml


from django.core.management.base import BaseCommand, CommandError

from django_countries import countries

from countrydemo.models import CountryInfo


def seed_country_info_models(seedfile):
    with open(seedfile, 'r') as f:
        data = yaml.load(f)
        notes = data['notes']
        for note in notes:
            print('{}, {}'.format(note['code'], note['note']))
            countryinfo, created = CountryInfo.objects.get_or_create(
                country=note['code'],
                notes=note['note'],
                )


def create_country_info_records():
    for val in list(countries):
        countryinfo, created = CountryInfo.objects.get_or_create(
            country=val[0])


class Command(BaseCommand):
    ''' 
    Seed our database
    '''
    help = dedent(__doc__).strip()

    def add_arguments(self, parser):
        '''

        '''
        parser.add_argument('--seedfile',
            help='Seed countries with info for the "notes" field'
            )
        parser.add_argument('--only-seedfile',
            action='store_true',
            default=False,
            help="Only create/or update records if they are in the seedfile",
            )


    def handle(self, *args, **options):
        print("options['seedfile'] = {}".format(options['seedfile']))

        if not options['only_seedfile']:
            create_country_info_records()
        if options['seedfile']:
            seed_country_info_models(options['seedfile'])
        #seed_country_info_models(options['seedfile'])

