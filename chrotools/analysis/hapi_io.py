import glob as g
import pandas as pd

from _hapiutils import GOVS, PROD, RACE, data_columns


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
    files = [x for x in g.glob(r'../data/*.txt.gz') if file_candidate in x]
    if len(files) is 0:
        print("No file found for given date...")
        print("Aborting...")
        return

    filename = files[0]
    planet_data = pd.read_csv(filename, sep=' ', comment='#', header=None)
    planet_data.columns = data_columns
    planet_data['Gov'] = planet_data['Gov'].apply(lambda x: GOVS[x])
    planet_data['Prod'] = planet_data['Prod'].apply(lambda x: PROD[x])
    planet_data['Race'] = planet_data['Race'].apply(lambda x: RACE[x])
    return planet_data