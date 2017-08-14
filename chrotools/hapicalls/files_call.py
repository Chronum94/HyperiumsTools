import datetime as dt
import gzip as gz
import requests as rq
import sys
from time import sleep


args = sys.argv
base_url = r'http://hyperiums.com/servlet/HAPI?game=Hyperiums8' \
           r'&player={}&passwd={}&request=download&filetype={}'

args.append('')
args = args[1:]

data_suffixes = ['alliances', 'events', 'players', 'planets']
data_file_mid = ['alliancelist', 'eventlist', 'playerlist', 'planetlist']
# date_prefix = dt.datetime.utcnow().strftime('%Y%m%d')

for key, data in enumerate(data_suffixes):

    print('Fetching', data, 'data.')
    args[-1] = data

    data_url = base_url.format(*args)
    data_response = rq.get(data_url)

    if data_response.status_code != 200:
        print('Bad response code! Something may be wrong.')
        sleep(1)
        continue

    if b'error' in data_response.content:
        print('You\'ve probably downloaded this today already.\n')
    else:
        data_dateline = gz.decompress(data_response.content).\
                    decode('utf-8').split('\n')[0]
        dt_from_file = dt.datetime.strptime(data_dateline[13:],
                                            '%Y-%m-%d %H:%M:%S')
        # dt_from_file = date_prefix
        file_date_string = dt_from_file.strftime('%Y%m%d')

        filename = file_date_string+'_'+data_file_mid[key]+'_Hyperiums8.txt.gz'
        full_filepath = r'../data/'+data_file_mid[key]+r'/'+filename

        with open(full_filepath, mode='wb') as record_file:
            record_file.write(data_response.content)

        print('Downloaded', data_file_mid[key], 'data.')
    sleep(3)
