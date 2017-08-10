import requests


class HapiAppPersonal:
    BASE_URL = r'www.hyperiums.com/servlet/HAPI'
    REQUEST_GAMES = r'?request=games'
    REQUEST_AUTH = r'?game={}&player=' \
                      r'{}&hapikey={}'

    def __init__(self, login_name, ext_auth_key, game_name='Hyperiums8'):
        self.login_name = login_name
        self.ext_auth_key = ext_auth_key
        self.game_name = game_name

        auth_data = requests.get(self.BASE_URL)
