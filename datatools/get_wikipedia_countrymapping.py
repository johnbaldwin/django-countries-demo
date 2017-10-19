
from collections import OrderedDict

from bs4 import BeautifulSoup
import requests

'''
<h2
    span id="Current_codes"
<table class="wikitable">

<tr>
<td><a href="/wiki/Western_Sahara" title="Western Sahara">Western Sahara</a></td>
<td><a href="/wiki/ISO_3166-1_alpha-2#EH" title="ISO 3166-1 alpha-2"><span style="font-family: monospace, monospace;">EH</span></a></td>
<td><span style="font-family: monospace, monospace;">ESH</span></td>
<td><span style="font-family: monospace, monospace;">732</span></td>
<td><a href="/wiki/ISO_3166-2:EH" title="ISO 3166-2:EH">ISO 3166-2:EH</a></td>
<td class="table-no" style="background:#F99;vertical-align:middle;text-align:center;">No</td>
</tr>




'''


def get_data(url):
    data = []
    # class="wikitable sortable
    results = requests.get(url)
    soup = BeautifulSoup(results.text, 'html.parser')
    span = soup.find(id='Current_codes')
    h2 = span.find_parent()
    table = h2.find_next_sibling('table')
    # Now do the interesting part
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        endpoint = cols[0].a['href']
        code2 = cols[1].span.text

        data.append({
            'countrycode': code2,
            'endpoint': endpoint,
        })

    return data


def write_data(data, siteinfo):
    print('---')
    print('data_source:')
    print('  label: "{}"'.format(siteinfo['label']))
    print('  url: "{}"'.format(siteinfo['url']))
    print('  host: "{}"'.format(siteinfo['host']))
    print('country_links:')
    for row in data:
        print('  - countrycode: "{}"'.format(row['countrycode']))
        print('    url: "{}{}"'.format(siteinfo['host'],row['endpoint']))

#def write_data2(file, data, siteinfo):
#    wi

def main():

    # TODO put into an OrderedDict
    siteinfo = OrderedDict({
        'url': "https://en.wikipedia.org/wiki/ISO_3166-1",
        'label': 'Wikipedia',
        'host': 'https://en.wikipedia.org',
        })
    data = get_data(siteinfo['url'])

    write_data(data, siteinfo)

 
if __name__ == '__main__':
    main()
