#!/usr/bin/env python
import sys
from math import log10


def _strfqty(qty):
    print("Qty is:", qty)
    number_of_digits = int(log10(qty))+1
    # print(number_of_digits)
    if 7 > number_of_digits > 3:
        return str(round(qty/1000, 1))+'k'
    elif 10 > number_of_digits > 6:
        return str(round(qty/1e6, 1))+'M'
    elif number_of_digits > 9:
        return str(round(qty/1e9, 1))+'B'


def _add_string_quantities(quantity_string):
    suffixes = ['K', 'M', 'B']
    suffix_muls = {'K': 1000, 'M': 1e6, 'B': 1e9}
    terms = [x.strip() for x in quantity_string.split(' + ')]
    print('Terms:', terms)
    significant_terms = [x for x in terms if
                         any([y in x for y in suffixes])]
    print("SigT:", significant_terms)
    terms = [float(x[:-1])*suffix_muls[x[-1]] for x in significant_terms]
    #print("Line 27:", terms)
    total = _strfqty(sum(terms))
    #print("Total:", total)
    return total


def has_enemy_fleet(lines):
    en_fleet_list = ['Enemy space AvgP:',
                     'PApx spat. ennemie:',
                     'Feindliche Flotten-AvgP:',
                     'Vijandige vloot GemS:']
    enemy_fleet_present = [(key+1, True) for key, val in enumerate(lines)
                           if any([val[0] == x for x in en_fleet_list])]
    if enemy_fleet_present:
        # print(lines[enemy_fleet_present[0][0]])
        return lines[enemy_fleet_present[0][0]][0]
    else:
        return '0'


def has_enemy_ga(lines):
    en_ga_list = ['Enemy ground AvgP',
                     'PApx terr. ennemie',
                     'Feindliche Boden-AvgP',
                     'Vijandige grond GemS']
    enemy_ga_present = [(key+1, True) for key, val in enumerate(lines)
                        if any([val[0] == x for x in en_ga_list])]
    if enemy_ga_present:
        # print(lines[enemy_ga_present[0][0]])
        return lines[enemy_ga_present[0][0]][0]
    else:
        return '0'


def has_friendly_fleet(lines):
    fr_fleet_list = ['Space AvgP:',
                     'PApx spatiale:',
                     'Flotten-AvgP:',
                     'Vloot GemS:']
    friend_fleet_present = [(key + 1, True) for key, val in enumerate(lines)
                            if any([val[0] == x for x in fr_fleet_list])]
    if friend_fleet_present:
        print("Friendly fleet qty sent:", lines[friend_fleet_present[0][0]][0])
        final_fr_fleet = _add_string_quantities(lines[friend_fleet_present[0][0]][0])
        return final_fr_fleet
    else:
        return '0'


def has_friendly_ga(lines):
    fr_ga_list = ['Ground AvgP:',
                     'PApx terrestre:',
                     'Boden-AvgP:',
                     'Grond GemS:']
    friend_ga_present = [(key + 1, True) for key, val in enumerate(lines)
                         if any([val[0] == x for x in fr_ga_list])]
    if friend_ga_present:
        ga_qty_string = lines[friend_ga_present[0][0]][0]
        if '%' in ga_qty_string:
            ga_qty_string = ga_qty_string[:-3]
        print('Fgt:', ga_qty_string)
        final_fr_ga = _add_string_quantities(ga_qty_string)
        return final_fr_ga
    else:
        return '0'


if '.txt' in sys.argv[1]:
    with open(sys.argv[1]) as f:
        lines = f.readlines()
else:
    lines = sys.argv[1]
lines = [x.strip().split('\t') for x in lines if x is not '\n']
name_coords = [x for x in lines[0] if x is not '']
energy = "nrg:"+lines[1][0]
stasis_status = [x[0] for x in lines if x[0] == 'Stasis'][0]

enemy_fleet_count = has_enemy_fleet(lines)
enemy_ga_count = has_enemy_ga(lines)
friendly_fleet_count = has_friendly_fleet(lines)
friendly_ga_count = has_friendly_ga(lines)
#print(enemy_fleet_count, enemy_ga_count)
print(enemy_fleet_count, enemy_ga_count, friendly_fleet_count, friendly_ga_count)
print(' '.join(name_coords), energy, stasis_status)
print('F:', friendly_fleet_count+'/'+friendly_ga_count, end=' ')
print('E:', enemy_fleet_count+'/'+enemy_ga_count)
