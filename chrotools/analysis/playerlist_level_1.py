# -*- coding: utf-8 -*-


def player_search(player_df, name):
    return player_df[player_df['Name'].str.contains(name)]

def player_list(player_df, filename_or_playerlist):
    if type(filename_or_playerlist) in [list, tuple]:
        players_in_list = player_df[
            player_df['Name'].isin(filename_or_playerlist)]
        return players_in_list
    elif '.txt' in filename_or_playerlist:
        try:
            with open(filename_or_playerlist) as f:
                playerlist = [x .strip() for x in f.readlines()]
                print(playerlist)
                players_in_list = player_df[
                    player_df['Name'].isin(playerlist)]
                return players_in_list
        except:
            raise

"""import hapi_io as hapi
df = hapi.read_player_list('20170813', 'Hyperiums8')
dizzydf = player_list(df, 'kek2.txt')
print(dizzydf)"""