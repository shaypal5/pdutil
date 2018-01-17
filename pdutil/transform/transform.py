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
    return df[[col for col in df.columns if col != y_col_lbl]], df[y_col_lbl]
