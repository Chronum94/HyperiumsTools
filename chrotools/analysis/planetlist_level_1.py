# -*- coding: utf-8 -*-
"""Level 1 planet analysis functions. These functions are defined by:

1. They require exactly 1 planetlist DataFrame to operate on.
2. They return exactly 1 planetlist DataFrame.

This implies that they operate only on one day's data.

This file contains the following functions:

1. planets_in_area(planet_df, cluster, extents)
2. planets_in_alliance(planet_df, alliance_tag, cluster='all')
"""


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
    if cluster == 'all':
        return planet_df[planet_df['Tag'] == alliance_tag]

    return planet_df[(planet_df['Tag'] == alliance_tag) &
                     (planet_df['SC'] == cluster)]

"""
import matplotlib.pyplot as plt
import hapi_io as hapi
df = hapi.read_planet_list('20170812', 'Hyperiums8')
# df = df[df['Civ'] > 20]
#panicdf = planets_in_alliance(df, '[Panic]', cluster=3)
plt.scatter(df['Civ'], df['Act'], marker='.', linewidths=0.1)
plt.show()
"""