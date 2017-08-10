import glob as g
import pandas as pd

import hapi_io


def planets_in_area(planet_df, cluster, extents):
    """Returns a list of planets in a rectangular area in a cluster.
    Inputs:
    =======
    planet_df (pandas DataFrame): DataFrame of planet data.

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


def planets_in_alliance(planet_df, alliance_tag, cluster='all'):
    """Returns a list of planets in a rectangular area in a cluster.
        Inputs:
        =======
        planet_df (pandas DataFrame): DataFrame of planet data.

        alliance_tag (str): The alliance tag for which to find the

        cluster (int): The number of the supercluster. By default
                        this is set to 'all', which will return
                        all planets of the alliance in all clusters.
                        If this is an integer, only planets from
                        that cluster will be returned.

        Output:
        =======
        planets_alliance (pandas DataFrame): DataFrame of planets within
                                            extents.
        """
    if cluster is 'all':
        planets_alliance = planet_df[planet_df['Tag'] == alliance_tag]
        return planets_alliance

    planets_alliance = planet_df[(planet_df['Tag'] == alliance_tag) &
                                 (planet_df['SC'] == cluster)]
    return planets_alliance

# print(hapi_io.read_planet_list('20170809', 'Hyperiums8').head())