"""Test pdutil.transform.or_by_masks."""

import pandas as pd

from pdutil.transform import or_by_masks


DF_DATA = [[23, 'Jo'], [19, 'Mi'], [15, 'Di']]
DF_IX = [1, 2, 3]
DF_COLS = ['Age', 'Name']


def test_base_case():
    df = pd.DataFrame(DF_DATA, DF_IX, DF_COLS)
    mask1 = pd.Series([False, True, True], df.index)
    mask2 = pd.Series([False, False, True], df.index)
    res_df = or_by_masks(df, [mask1, mask2])
    assert 1 not in res_df.index
    for ix in [2, 3]:
        assert ix in res_df.index


def test_no_masks():
    df = pd.DataFrame(DF_DATA, DF_IX, DF_COLS)
    res_df = or_by_masks(df, [])
    for ix in [1, 2, 3]:
        assert ix in res_df.index


def test_one_mask():
    df = pd.DataFrame(DF_DATA, DF_IX, DF_COLS)
    mask2 = pd.Series([False, False, True], df.index)
    res_df = or_by_masks(df, [mask2])
    assert 1 not in res_df.index
    assert 2 not in res_df.index
    assert 3 in res_df.index


BIG_DF_DATA = [[3, 'A'], [1, 'D'], [4, 'C'], [6, 'G'], [2, 'W']]
BIG_DF_IX = [1, 2, 3, 4, 5]
BIG_DF_COLS = ['Num', 'Char']


def test_three_masks():
    df = pd.DataFrame(BIG_DF_DATA, BIG_DF_IX, BIG_DF_COLS)
    mask1 = pd.Series([False, False, True, True, True], df.index)
    mask2 = pd.Series([False, False, False, True, True], df.index)
    mask3 = pd.Series([True, False, False, True, True], df.index)
    res_df = or_by_masks(df, [mask1, mask2, mask3])
    assert 2 not in res_df.index
    for ix in [1, 3, 4, 5]:
        assert ix in res_df.index
