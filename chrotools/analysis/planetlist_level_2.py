# -*- coding: utf-8 -*-
"""Level 2 planet analysis functions. These functions are defined by:

!! These specifications are tentative and may change.
1. They require exactly 2 planetlist DataFrames to operate on.
2. They return exactly 1 planetlist DataFrame.

This implies that they operate only on two days' data.

"""
import pandas as pd

import hapi_io as hapi
import planetlist_level_1 as lev


def planets_new_in_area(from_date,
                        to_date, cluster, extents, game='Hyperiums8'):
    """Takes two dates (in 'YYYYMMDD' form), a cluster number, and
    extents. Returns any new planets that have appeared in the area
    in the interval of time.

    Inputs:
    =======
    from_date (str): YYYYMMDD format datestring from where to start
                    interval.
    to_date (str): YYYYMMDD format datestring to where the interval
                    hoes.
    extents (list or tuple): [xmin, xmax, ymin, ymax] coordinate
                    extents in which to check for new planets.
    cluster (int): The supercluster in which to search.

    Output:
    =======
    new_planets (pandas DataFrame): DataFrame of new planets in the
                area.

    """
    planets_from_date = hapi.read_planet_list(from_date, game)
    planets_to_date = hapi.read_planet_list(to_date, game)

    planets_from_area = lev.planets_in_area(planets_from_date,
                                            cluster, extents)
    planets_to_area = lev.planets_in_area(planets_to_date, cluster, extents)

    return planets_to_area[~planets_to_area['ID'].isin(planets_from_area['ID'])]

# print(planets_new_in_area('20170809', '20170810', 3, [-30, 30, -30, 30]))
