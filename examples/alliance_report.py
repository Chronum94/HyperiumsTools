from chrotools.analysis.planetlist_level_2 import *

import pandas as pd

from chrotools.analysis.planetlist_level_2 import planet_moves_between_area

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
pd.set_option('display.max_rows', 500)

from_date = '20170820'
to_date = '20170821'
extents = [-30, 0, -30, -1]
print('Planet change report from', from_date, 'to', to_date)
print('In', *extents)
delta_gov = planets_gov_change_area(from_date, to_date, 3,
                                    [-30, 30, -30, 30]) \
[['Name_y', 'x_y', 'y_y', 'SC_y', 'Gov_x', 'Gov_y', 'Tag_y']]
delta_gov.columns = ['Name', 'x', 'y', 'SC', 'Prev gov',
                     'Curr gov', 'Curr tag']
delta_gov.reset_index(inplace=True)
print('Gov changes:')
print(delta_gov, '\n')


delta_tag = planets_tag_change_area(from_date, to_date, 3,
                                    [-30, 30, -30, 30]) \
[['Name_y', 'x_y', 'y_y', 'SC_y', 'Gov_y', 'Tag_x', 'Tag_y']]
delta_tag.columns = ['Name', 'x', 'y', 'SC', 'Curr gov.',
                     'Prev tag', 'Curr tag']
delta_tag.reset_index(inplace=True)
print('Tag changes:')
print(delta_tag, '\n')


delta_planet = planets_new_area(from_date, to_date, 3, [-30, 30, -30, 30])
delta_planet.reset_index(inplace=True)
print('New planets:')
print(delta_planet)

print(planet_moves_between_area(from_date, to_date, 1, 3))
