# -*- coding: utf-8 -*-

import glob as g
import pandas as pd

from _hapiutils import GOVS, PROD, RACE, planet_cols, player_cols

__all__ = ['read_planet_list', 'read_player_list']


def read_planet_list(date, game_name):
    """Returns a pandas DataFrame of planet data for the given date
    and game.
    Inputs:
    =======
    date (str): Str containing the date of the planetlist file in
                YYYYMMDD form. Eg: '20170131' for 31-Jan-2017.

    game_name (str): Str containing the game name. Eg: Hyperiums8 for
                        Hyperiums Perm Round 8.

    Output:
    =======
    planet_data (pandas DataFrame): DataFrame of planet data."""
    file_candidate = date+'_planetlist_'+game_name
    files = [x for x in g.glob(r'../data/planetlist/*.txt.gz')]#  if file_candidate in x]
    print(files)
    if not files:
        print("No file found for given date...")
        print("Aborting...")
        raise FileNotFoundError

    filename = files[0]
    planet_data = pd.read_csv(filename, sep=' ', comment='#')
    planet_data.columns = planet_cols
    planet_data['Gov'] = planet_data['Gov'].apply(lambda x: GOVS[x])
    planet_data['Prod'] = planet_data['Prod'].apply(lambda x: PROD[x])
    planet_data['Race'] = planet_data['Race'].apply(lambda x: RACE[x])
    return planet_data


def read_player_list(date, game_name):
    """Returns a pandas DataFrame of player data for the given date
    and game.
    Inputs:
    =======
    date (str): Str containing the date of the playerlist file in
                YYYYMMDD form. Eg: '20170131' for 31-Jan-2017.

    game_name (str): Str containing the game name. Eg: Hyperiums8 for
                        Hyperiums Perm Round 8.

    Output:
    =======
    planet_data (pandas DataFrame): DataFrame of player data."""
    file_candidate = date+'_playerlist_'+game_name
    files = [x for x in g.glob(r'../data/playerlist/*.txt.gz') if file_candidate in x]
    if not files:
        print("No file found for given date...")
        print("Aborting...")
        raise FileNotFoundError

    filename = files[0]

    player_data = pd.read_csv(filename, sep=' ', comment='#', header=None,
                              usecols=range(9))  # Don't care about country.
    player_data.columns = player_cols
    # print(player_data)
    return player_data

"""print(read_player_list('20170812', 'Hyperiums8'))
"""
