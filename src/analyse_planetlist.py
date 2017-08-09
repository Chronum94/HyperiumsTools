import glob as g
import pandas as pd

import _hapiutils as hapi


def read_planet_list(date, game_name):
    """Returns a pandas DataFrame of planet data for the given date
    and """
    file_candidate = date+'_planetlist_'+game_name
    files = [x for x in g.glob(r'../data/*.txt.gz') if file_candidate in x]
    if len(files) is not 1:
        print("Either no file exists for this date, or too many files.")
        print("Aborting...")
        return

    filename = files[0]
    planet_data = pd.read_csv(filename, sep=' ', comment='#', header=None)
    planet_data.columns = hapi.data_columns
    return planet_data


def planets_in_area(planet_df, cluster, extents):
    """Returns a list of planets in a rectangular area in a cluster.
    Inputs:
    =======
    planet_df (pandas DataFrame): DataFrame of complete planet data.

    cluster (int): The number of the supercluster.

    extents (list, iterable): List/tuple of 4 integers.
                                [xmin, xmax, ymin, ymax]

    Output:
    =======
    planets_extents (pandas DataFrame): DataFrame of planets within
                                        extents.
    """

    xmin, xmax, ymin, ymax = extents
    planets_extents = planet_df[(planet_df['SC'] == cluster) &
                                (planet_df['x'].between(xmin, xmax)) &
                                (planet_df['y'].between(ymin, ymax))]
    return planets_extents

# print(planets_in_area(df, 3, [9, 12, -12, -9]).head(n=10))
# print(df[df['Name'] == 'FortreDoom'])
# print(df['Race'].head())

print(read_planet_list('20170809', 'Hyperiums8').head())