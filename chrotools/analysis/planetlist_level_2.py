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


def _planets_common_in_frame(df1, df2, by='ID'):
    return df1.join(df2, on=by, how='inner', rsuffix='_r')


def planets_new_area(from_date,
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


def planets_gov_change_area(from_date,
                            to_date, cluster, extents, from_gov='any',
                            to_gov='Dict', game='Hyperiums8'):
    """Takes two dates (in 'YYYYMMDD' form), a cluster number, extents,
    the government from, and the government to which the planets are
    changed. Returns planets whose governments have changed from
    from_gov to to_gov in the interval of time.

    Inputs:
    =======
    from_date (str): YYYYMMDD format datestring from where to start
                    interval.
    to_date (str): YYYYMMDD format datestring to where the interval
                    hoes.
    cluster (int): The supercluster in which to search.
    extents (list or tuple): [xmin, xmax, ymin, ymax] coordinate
                    extents in which to check for new planets.
    from_gov (str): The previous day's government. 'Demo', 'Auth' or
                    'Dict'. Default 'all'. If set to 'all', all
                    governments that are not to_gov will be selected.
    to_gov (str): The current day's government. Same strings as
                    from_gov, but not 'all'. Default 'Dict'.

    Output:
    =======
    gov_changed_planets (pandas DataFrame): DataFrame of gov-changed
                    planets in the area.

    """
    planets_from_date = hapi.read_planet_list(from_date, game)
    planets_to_date = hapi.read_planet_list(to_date, game)

    planets_from_area = lev.planets_in_area(planets_from_date,
                                            cluster, extents)
    planets_to_area = lev.planets_in_area(planets_to_date, cluster, extents)

    if from_gov == 'any':
        planets_from_gov = planets_from_area[planets_from_area['Gov'] != to_gov]
    else:
        planets_from_gov = planets_from_area[planets_from_area['Gov'] ==
                                             from_gov]
    planets_to_gov = planets_to_area[planets_to_area['Gov'] == to_gov]

    planets_gov_changed = _planets_common_in_frame(planets_to_gov,
                                                   planets_from_gov)
    return planets_to_gov[planets_to_gov['ID'].isin(planets_gov_changed['ID'])]


# print(planets_gov_change_area('20170810', '20170811', 3, [-30, 0, -30, -1]))
