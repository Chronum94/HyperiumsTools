# -*- coding: utf-8 -*-

# Dicts mapping HAPI return values to human-readable values.

__all__ = ['GOVS', 'PROD', 'RACE', 'planet_cols', 'player_cols']

GOVS = {0: 'Dict', 1: 'Auth', 2: 'Demo', 3: 'Hyps'}
RACE = {0: 'H', 1: 'A', 2: 'X'}
PROD = {0: 'T', 1: 'M', 2: 'A'}

planet_cols = ['ID', 'Name', 'Gov', 'x', 'y', 'Race', 'Prod', 'Act', 'Tag',
                'Civ', 'Size', 'SC']
player_cols = ['Name', 'InfR', 'InfRSC', 'Influ', 'HypR', 'IDRR', 'IDR',
               'IDRRSC', 'SC']
