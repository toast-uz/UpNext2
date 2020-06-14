'''
Open Data for Public Transportation dump module for UpNext
Copyright(c) 2020 Tatsuzo Osawa
All rights reserved. This program and the accompanying materials
are made available under the terms of the MIT License:
    https: // opensource.org/licenses/mit-license.php
'''

import requests
from . import config_secret

query_string = ('https://api-tokyochallenge.odpt.org/api/v4/odpt:{}.json'
                '?acl:consumerKey={}')
save_path = 'local_data/odpt_dump/{}.json'


def get_and_save(rdf_type):
    url = query_string.format(rdf_type, config_secret.apikey)
    print('Getting {}...'.format(rdf_type), end='', flush=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path.format(rdf_type), 'wb') as save_file:
            save_file.write(response.content)
        print('done.')
    except Exception as e:
        print('fail, due to: {}'.format(e))
        raise


if __name__ == '__main__':
    for rdf_type in [
            'Calender',
            'Operator',
            'Station',
            'StationTimetable',
            'TrainTimetable',
            'TrainType',
            'RailDirection',
            'Railway']:
        get_and_save(rdf_type)
