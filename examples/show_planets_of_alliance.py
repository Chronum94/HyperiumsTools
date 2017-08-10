import seaborn as sns
import matplotlib.pyplot as plt

import analysis.analyse_planetlist as pl


tag = '[Panic]'
today, yesterday = '20170810', '20170809'
game = 'Hyperiums8'

# Get planet list for two days.
planet_data_yeste = pl.read_planet_list(yesterday, game)
planet_data_today = pl.read_planet_list(today, game)

# Get alliance planet list.
panic_tagged_yeste = pl.planets_in_alliance(planet_data_yeste, tag, cluster=3)
panic_tagged_today = pl.planets_in_alliance(planet_data_today, tag, cluster=3)

print('Average planet activity previously in', tag)
print(round(panic_tagged_yeste['Act'].mean()), '\n')
print('Average planet activity currently in', tag)
print(round(panic_tagged_today['Act'].mean()))
