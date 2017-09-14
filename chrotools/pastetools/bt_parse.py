import pandas as pd


def parse_bt(bt_clipboard):
    df = pd.read_clipboard(sep='')
    print(df)

parse_bt('Kek')
