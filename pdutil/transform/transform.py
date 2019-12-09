"""Transformation-related pandas utilities."""


def x_y_by_col_lbl(df, y_col_lbl):
    """Returns an X dataframe and a y series by the given column name.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to split.
    y_col_lbl : object
        The label of the y column.

    Returns
    -------
    X, y : pandas.DataFrame, pandas.Series
        A dataframe made up of all columns but the column with the given name
        and a series made up of the same column, respectively.

    Example
    -------
    >>> import pandas as pd
    >>> data = [[23, 'Jo', 4], [19, 'Mi', 3]]
    >>> df = pd.DataFrame(data, [1, 2] , ['Age', 'Name', 'D'])
    >>> X, y = x_y_by_col_lbl(df, 'D')
    >>> X
       Age Name
    1   23   Jo
    2   19   Mi
    >>> y
    1    4
    2    3
    Name: D, dtype: int64
    """
    x_cols = [col for col in df.columns if col != y_col_lbl]
    return df[x_cols], df[y_col_lbl]


def x_y_by_col_lbl_inplace(df, y_col_lbl):
    """Breaks the given dataframe into  an X frame and a y series by the given
    column name.

    The original frame is returned, without the y series column, as the X
    frame, so no new dataframes are created.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to split.
    y_col_lbl : object
        The label of the y column.

    Returns
    -------
    X, y : pandas.DataFrame, pandas.Series
        A dataframe made up of all columns but the column with the given name
        and a series made up of the same column, respectively.

    Example
    -------
    >>> import pandas as pd
    >>> data = [[23, 'Jo', 4], [19, 'Mi', 3]]
    >>> df = pd.DataFrame(data, [1, 2] , ['Age', 'Name', 'D'])
    >>> X, y = x_y_by_col_lbl(df, 'D')
    >>> X
       Age Name
    1   23   Jo
    2   19   Mi
    >>> y
    1    4
    2    3
    Name: D, dtype: int64
    """
    y = df[y_col_lbl]
    df.drop(labels=y_col_lbl, axis=1, inplace=True)
    return df, y


def or_by_masks(df, masks):
    """Returns a sub-dataframe by the logical or over the given masks.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to take a subframe of.
    masks : list
        A list of pandas.Series of dtype bool, indexed identically to the given
        dataframe.

    Returns
    -------
    pandas.DataFrame
        The sub-dataframe resulting from applying the masks to the dataframe.

    Example
    -------
    >>> import pandas as pd
    >>> data = [[23, 'Jo'], [19, 'Mi'], [15, 'Di']]
    >>> df = pd.DataFrame(data, [1, 2, 3] , ['Age', 'Name'])
    >>> mask1 = pd.Series([False, True, True], df.index)
    >>> mask2 = pd.Series([False, False, True], df.index)
    >>> or_by_masks(df, [mask1, mask2])
       Age Name
    2   19   Mi
    3   15   Di
    """
    if len(masks) < 1:
        return df
    if len(masks) == 1:
        return df[masks[0]]
    overall_mask = masks[0] | masks[1]
    for mask in masks[2:]:
        overall_mask = overall_mask | mask
    return df[overall_mask]


def or_by_mask_conditions(df, mask_conditions):
    """Returns a sub-dataframe by the logical-or over given mask conditions,

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to take a subframe of.
    mask_conditions : list
        A list of functions that, when applied to a dataframe, produce each a
        pandas.Series of dtype bool, indexed identically to the dataframe.

    Returns
    -------
    pandas.DataFrame
        The sub-dataframe resulting from applying the mask conditions to the
        dataframe.

    Example
    -------
    >>> import pandas as pd
    >>> data = [[23, 'Jo'], [19, 'Mi'], [15, 'Di']]
    >>> df = pd.DataFrame(data, [1, 2, 3] , ['Age', 'Name'])
    >>> mask_cond1 = lambda df: df.Age < 18
    >>> mask_cond2 = lambda df: df.Age > 20
    >>> or_by_mask_conditions(df, [mask_cond1, mask_cond2])
       Age Name
    1   23   Jo
    3   15   Di
    """
    return or_by_masks(df, [cond(df) for cond in mask_conditions])


def generate_lags(df, lags=None, columns=None, fill_value=None, dropna=None):
    """Generate lags of columns in the given dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to generage lags for.
    lags : list of int, optional
        A list of the lags to generate. If an integer is given instead, it is
        interpreted as the maximum lag to generate, and all integer lags up
        to it are generated. E.g. providing lags=4 corresponds to providing
        lags=[1, 2, 3, 4].
    columns : list of str, optional
        The labels of columns for which to generate lags. If not given, lags
        are generated for all columns.
    fill_value : object, optional
        The scalar value to use for newly introduced missing values. See the
        documentation of the corresponding parameter of the
        pandas.DataFrame.shift method for more information.
    dropna : bool, optional
        If set to True, all rows containing null values are dropped. If
        fill_value is not provided this results in trimming all columns to
        their overall intersection.

    Returns
    -------
    pandas.DataFrame
        The dataframe containing all generated lags.

    Example
    -------
    >>> import pandas as pd
    >>> data = [[1], [2], [3], [4], [5]]
    >>> df = pd.DataFrame(data, [1, 2, 3, 4, 5] , ['p'])
    >>> generate_lags(df, lags=2, dropna=True)
        p  p1  p2
    3   3  2   1
    4   4  3   2
    5   5  4   3
    """
    if isinstance(lags, int):
        lags = list(range(1, lags + 1))
    all_lags = {}
    all_columns = []
    for colbl in df.columns:
        col = df[colbl]
        clags = {f'{colbl}-{i}': col.shift(i) for i in lags}
        clags[colbl] = col
        all_lags.update(clags)
        clbls = [colbl] + [f'{colbl}-{i}' for i in lags)
        all_columns.extend(clbls)
