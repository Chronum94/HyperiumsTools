import seaborn as sns
import matplotlib.pyplot as plt

from chrotools.analysis.hapi_io import *
from chrotools.analysis.planetlist_level_1 import *


tag = '[Mafi@]'
today, yesterday = '20170828', '20170826'
game = 'Hyperiums8'

# Get planet list for two days.
planet_data_yeste = read_planet_list(yesterday, game)
planet_data_today = read_planet_list(today, game)

# Get alliance planet list.
panic_tagged_yeste = planets_in_alliance(planet_data_yeste, tag, cluster=1)
panic_tagged_today = planets_in_alliance(planet_data_today, tag, cluster=1)

"""print('Average planet activity previously in', tag)
print(round(panic_tagged_yeste['Act'].mean()), '\n')
print('Average planet activity currently in', tag)
print(round(panic_tagged_today['Act'].mean()))"""
print(len(panic_tagged_yeste), len(panic_tagged_today))
