import requests


class HapiAppPersonal:
    BASE_URL = r'http://www.hyperiums.com/servlet/HAPI?'
    REQUEST_GAMES = r'request=games'
    REQUEST_AUTH = r'game={}&player=' \
                      r'{}&hapikey={}'



    request_auth_tokens = None

    def __init__(self, login_name, ext_auth_key, game_name='Hyperiums8'):
        self.login_name = login_name
        self.ext_auth_key = ext_auth_key
        self.game_name = game_name

        self.auth_data = requests.get(self.BASE_URL +
                                      self.REQUEST_AUTH.format(game_name,
                                                               login_name,
                                                               ext_auth_key))
        self.auth_response = dict([x.split('=') for x in
                                   self.auth_data.text.split('&')])

        self.request_auth_tokens = [self.auth_response['gameid'],
                                    self.auth_response['playerid'],
                                    self.auth_response['authkey']]

        self.REQUEST_URL_PREFIX ='gameid={}&playerid={}&authkey={}&'\
            .format(*self.request_auth_tokens)
        print(self.REQUEST_URL_PREFIX)

    def foreign_fleets(self):
        foreign_fleets_url = 'request=getfleetsinfo&planet=*' \
                                 '&data=foreign_planets'

        url = self.BASE_URL+self.REQUEST_URL_PREFIX+foreign_fleets_url
        data = requests.get(url).text
        print(data)

