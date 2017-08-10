

class HapiAppPersonal:
    BASE_URL = r'www.hyperiums.com/servlet/HAPI'
    REQUEST_GAMES = r'?request=games'
    REQUEST_AUTH = r'?game=$gamename&player=' \
                      r'$login_name&hapikey=$ext_auth_key'

    def __init__(self, login_name, ext_auth_key):
